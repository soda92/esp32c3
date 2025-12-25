import machine
import ssd1306
import time

# --- CONFIGURATION ---
SDA_PIN = 5
SCL_PIN = 6
# Try 32 first. If you have black space at the bottom, try 48 or 64.
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 32

i2c = machine.SoftI2C(sda=machine.Pin(SDA_PIN), scl=machine.Pin(SCL_PIN))
oled = ssd1306.SSD1306_I2C(SCREEN_WIDTH, SCREEN_HEIGHT, i2c)

# 3x5 Bitmap Font for Digits 0-9
DIGITS = [
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],  # 0
    [0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1],  # 1
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],  # 2
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],  # 3
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1],  # 4
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],  # 5
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],  # 6
    [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],  # 7
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],  # 8
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],  # 9
]


def draw_digit(num, x, y, size):
    if 0 <= num <= 9:
        bitmap = DIGITS[num]
        for i in range(15):
            if bitmap[i]:
                oled.fill_rect(x + (i % 3 * size), y + (i // 3 * size), size, size, 1)


count = 0

while True:
    oled.fill(0)

    # 1. Draw Header (Small Text)
    # If height is small (32), we put header at Y=0
    oled.text("COUNT:", 2, 0)

    # 2. Draw Big Numbers
    s_count = str(count)

    # Dynamic Sizing:
    # If screen is 32px tall, use Scale 3 (Digit height 15px).
    # If screen is 64px tall, use Scale 5 (Digit height 25px).
    if SCREEN_HEIGHT <= 32:
        scale = 3
        y_pos = 12  # Place below the header
    else:
        scale = 5
        y_pos = 20

    # Center the number block horizontally
    digit_width = 3 * scale
    total_width = len(s_count) * (digit_width + scale)
    start_x = (SCREEN_WIDTH - total_width) // 2

    for i, char in enumerate(s_count):
        # x position + spacing (1 scale unit gap)
        draw_digit(int(char), start_x + (i * (digit_width + scale)), y_pos, scale)

    # 3. Debug Border (Optional)
    # Draws a box around the screen edges so you can see if physical clipping happens
    oled.rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 1)

    oled.show()
    count += 1
    time.sleep(0.1)
