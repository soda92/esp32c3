PORT = /dev/esp32c3
BAUD = 460800

# Default action: run the main.py on the board
run:
	mpremote connect $(PORT) run main.py

# Open REPL
repl:
	mpremote connect $(PORT) repl

# Sync: Copy all .py files to board
sync:
	mpremote connect $(PORT) fs cp *.py :

# Wipe and Flash (Careful!)
flash:
	esptool.py --port $(PORT) erase_flash
	esptool.py --port $(PORT) --baud $(BAUD) write_flash -z 0x0 firmware.bin
