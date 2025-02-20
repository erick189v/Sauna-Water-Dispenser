import time
import onewire

class DS18X20:
    def __init__(self, onewire_bus):
        self.ow = onewire_bus

    def scan(self):
        return [rom for rom in self.ow.scan() if rom[0] == 0x28]

    def convert_temp(self):
        """Send command to start temperature conversion"""
        self.ow.reset()
        self.ow.writebyte(0xCC)  # Skip ROM command
        self.ow.writebyte(0x44)  # Convert T command

    def read_temp(self, rom):
        """Read the temperature from a DS18B20 sensor"""
        self.ow.reset()
        self.ow.select_rom(rom)
        self.ow.writebyte(0xBE)  # Read Scratchpad

        data = self.ow.read_bytes(9)
        temp = data[0] | (data[1] << 8)  # Combine low and high bytes

        if temp & 0x8000:  # Negative temperature
            temp = -((temp ^ 0xFFFF) + 1)

        return temp / 16.0  # Convert raw data to Celsius
