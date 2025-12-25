import machine
import ssd1306
import time

# --- CONFIGURATION (Based on your scan) ---
SDA_PIN = 5
SCL_PIN = 6
I2C_ADDR = 0x3C
WIDTH = 128
HEIGHT = 64

# 1. Setup I2C
# The ESP32-S3 has hardware I2C, but SoftI2C is more robust for pin swapping
i2c = machine.SoftI2C(sda=machine.Pin(SDA_PIN), scl=machine.Pin(SCL_PIN), freq=400000)

# 2. Setup Display
oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=I2C_ADDR)


# Helper function to center text
def center_text(text, y_pos):
    # Default font is 8 pixels wide per character
    text_width = len(text) * 8
    x_pos = (WIDTH - text_width) // 2
    oled.text(text, x_pos, y_pos)


counter = 0

while True:
    # A. Clear screen (set all pixels to black)
    oled.fill(0)

    # B. Draw "GUI" elements (White Rectangle Border)
    # rect(x, y, w, h, color)
    oled.rect(0, 0, WIDTH, HEIGHT, 1)

    # C. Draw Header
    center_text("STATUS", 5)

    # D. Draw the Number
    # We can't scale the font easily, but we can center it
    display_str = f"Count: {counter}"
    center_text(display_str, 30)

    # E. Draw a progress bar line at the bottom
    # line(x1, y1, x2, y2, color)
    progress = counter % 128  # loop bar every 128 counts
    oled.line(0, 55, progress, 55, 1)

    # F. Push to display
    oled.show()

    counter += 1
    time.sleep(0.1)
