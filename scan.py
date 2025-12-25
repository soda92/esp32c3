# Save as scan.py and run with: mpremote run scan.py
import machine

# Try the most common S3 SuperMini I2C pairs
pairs = [(8, 9), (5, 6), (1, 2), (4, 5), (11, 12)]

print("Scanning for display...")

for sda_pin, scl_pin in pairs:
    try:
        i2c = machine.SoftI2C(sda=machine.Pin(sda_pin), scl=machine.Pin(scl_pin))
        devices = i2c.scan()
        if devices:
            print(
                f"Found device at address {hex(devices[0])} using SDA={sda_pin}, SCL={scl_pin}"
            )
            break
    except Exception:
        pass
else:
    print("No display found. Check if it's plugged in correctly.")
