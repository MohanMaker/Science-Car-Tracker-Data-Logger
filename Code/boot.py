import board
import digitalio
import storage

switch = digitalio.DigitalInOut(board.D1)

switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

if switch.value is True:
    output = False
else:
    output = True

# If the switch pin is connected to ground (switch is pressed), the computer (not CircuitPython) can write to the drive
storage.remount("/", output)