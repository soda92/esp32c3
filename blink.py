import machine
import time

# Pin numbers vary by board "Bottle" shape.
# Generic C3 often uses GPIO 8 or 2 for the onboard LED.
# If yours is the XIAO ESP32C3, the LED is likely strictly internal or on a different pin.
pin = machine.Pin(8, machine.Pin.OUT)


def off():
    pin.value(1)


def on():
    pin.value(0)


span = 0.3


def pause():
    time.sleep(span)


COUNT = 3


while True:
    for _ in range(COUNT):
        on()
        pause()
        off()
        pause()
    off()
    time.sleep(3)
