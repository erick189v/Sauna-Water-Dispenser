# Sauna-Water-Dispenser
A Raspberry Pi Pico W project that automates a sauna cooling system based on temperature readings.
# Sauna Automation with Raspberry Pi Pico W 🚀🔥

**Project Overview**  
This project automates a **sauna cooling system** using **Raspberry Pi Pico W**.  
- 🌡️ Reads temperature using **DS18B20 sensor**.  
- 🚿 Activates a **water pump** when sauna gets too hot.  
- 🌐 Runs a **web server** to manually control the pump.  

## 💻 Tech Stack  
- **MicroPython**  
- **Raspberry Pi Pico W**  
- **DS18B20 Temperature Sensor**  
- **Relay Module & Water Pump**  

## 🚀 Features  
✅ **Real-time temperature monitoring**  
✅ **Automatic water spray activation**  
✅ **Web interface for manual control**  

## 📷 Project Demo  


## 🛠️ Required Components & Tools  

| Component            | Description                          |
|----------------------|--------------------------------------|
| 🔥 **Raspberry Pi Pico W**  | The microcontroller running MicroPython |
| 🌡️ **DS18B20 Sensor** | Waterproof temperature sensor |
| 🔌 **Relay Module** | Controls the water pump |
| 🚿 **Water Pump** | Dispenses water when needed |
| ⚡ **12V Power Supply** | Powers the pump |
| 🔗 **Jumper Wires** | For connecting components |
| 🔲 **Breadboard (Optional)** | For prototyping |
| 🔧 **WAGO Connectors (Optional)** | For secure wiring |

📌 **Full Wiring Guide**: Follow this tutorial:  
🔗 [Raspberry Pi Pico W with DS18B20 Sensor](https://randomnerdtutorials.com/raspberry-pi-pico-ds18b20-micropython/)  

---

## 🔌 Wiring Guide  

| **DS18B20 Pin** | **Connect To** |
|----------------|---------------|
| Red (VCC)      | 3.3V (Pico W) |
| Black (GND)    | GND (Pico W)  |
| Yellow (Data)  | GP0 (Pico W)  |
| **4.7kΩ Resistor** | Between **VCC** and **Data** |

| **Relay Module Pin** | **Connect To** |
|----------------------|---------------|
| **VCC**  | 5V (Pico W) |
| **GND**  | GND (Pico W) |
| **IN**   | GP21 (Pico W) |
| **NO**   | Water Pump + |
| **COM**  | 12V Power Supply + |

---

## 🛠️ How to Install & Run  

1️⃣ **Clone the repository:**
```sh
git clone https://github.com/your-username/sauna-automation.git
cd sauna-automation
