from controller import Gamepad
import uinput
from time import sleep
from random import choice

def wolf_main():
    wolf_keys = [uinput.KEY_RIGHT,
                 uinput.KEY_LEFT,
                 uinput.KEY_UP,
                 uinput.KEY_DOWN,
                 uinput.KEY_RIGHTSHIFT,
                 uinput.KEY_RIGHTCTRL,
                 uinput.KEY_RIGHTALT,
                 uinput.KEY_SPACE]
    wolf_device = Gamepad(wolf_keys)
    sleep(1)
    while True:
        curr_key = choice(wolf_keys)
        wolf_device.hold_key_for(curr_key, 1)
        sleep(0.1)
