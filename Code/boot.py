import board
import digitalio
import storage

switch = digitalio.DigitalInOut(board.D0)

switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

output = True
if switch.value is True:
    output = False
else:
    output = True

storage.remount("/", output)