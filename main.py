import network
import socket
import machine
import time
import secrets
import _thread
import ds18x20
import onewire

# **Wi-Fi Credentials**
ssid = secrets.secrets["ssid"]
password = secrets.secrets["password"]

# **GPIO Configurations**
RELAY_PIN = machine.Pin(21, machine.Pin.OUT)  # Relay (Pump)
DS_PIN = machine.Pin(22)  # DS18B20 Data Pin

# **Initialize DS18B20**
ds_sensor = ds18x20.DS18X20(onewire.OneWire(DS_PIN))
roms = ds_sensor.scan()  

# **Temperature Threshold**
TEMP_THRESHOLD = 70  # Adjust based on sauna needs

print("Sauna Automation Started...")

# **Connect to Wi-Fi**
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

print("Connecting to Wi-Fi...")
while not wlan.isconnected():
    time.sleep(1)

print("✅ Connected! IP Address:", wlan.ifconfig()[0])


def temperature_control():
    while True:
        if not roms:
            print("⚠️ No DS18B20 sensor found! Check wiring.")
        else:
            ds_sensor.convert_temp()
            time.sleep(1)  # ✅ Allow time for conversion

            for rom in roms:
                temp_c = ds_sensor.read_temp(rom)  # ✅ FIXED: Proper temperature reading
                print(f"🌡️ Temperature: {temp_c:.2f}°C")

                if temp_c < TEMP_THRESHOLD:
                    print("⚠️ Temperature is LOW! Turning ON the pump.")
                    RELAY_PIN.value(1)
                    time.sleep(5)
                    RELAY_PIN.value(0)
                else:
                    print("✅ Temperature is OK. Waiting 5 minutes.")

        time.sleep(5*60)  # Check every 5 minutes

# **Start the Temperature Control in a Separate Thread**
_thread.start_new_thread(temperature_control, ())


# **Web Server to Manually Activate the Pump**
def web_page(temp):
    return f"""<!DOCTYPE html>
<html>
<head>
    <title>Sauna Control</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {{ font-family: Arial, sans-serif; text-align: center; background-color: #f4f4f4; }}
        h1 {{ color: #333; }}
        .button {{ padding: 15px 30px; font-size: 20px; border: none; color: white; background-color: #007BFF; cursor: pointer; border-radius: 10px; }}
        .button:hover {{ background-color: #0056b3; }}
        .status {{ font-size: 24px; color: #555; margin-top: 20px; }}
    </style>
</head>
<body>
    <h1>🔥 Sauna Temperature Control</h1>
    <p class="status">🌡️ Current Temperature: <strong>{temp:.2f}°C</strong></p>
    <form action="/pump_on" method="get">
        <button class="button">Activate Water Pump</button>
    </form>
</body>
</html>
"""


# **Start the Web Server**
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 8081))
server_socket.listen(5)

print("🌐 Web Server Running at:", wlan.ifconfig()[0])

while True:
    conn, addr = server_socket.accept()
    request = conn.recv(1024).decode()

    if roms:
        ds_sensor.convert_temp()  # ✅ Correct function
        time.sleep(1)
        temp_c = ds_sensor.read_temp(roms[0])  # ✅ Correct function
    else:
        temp_c = -99

    print("Request:", request)

    # Handle Web Requests
    if "/pump_on" in request:
        print("⚡ Manual Pump Activation!")
        RELAY_PIN.value(1)
        time.sleep(5)
        RELAY_PIN.value(0)

    # Send HTTP response
    response = web_page(temp_c)
    conn.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection: close\r\n\r\n" + response)
    conn.close()
