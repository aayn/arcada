import uinput
from time import sleep

class Gamepad(uinput.Device):
    def __init__(self, key_list):
        uinput.Device.__init__(self, key_list)
        self.key_list = key_list

    def press_key(self, key):
        # u_key = getattr(uinput, "KEY_" + key)
        self.emit_click(key)

    def hold_key(self, key):
        u_key = getattr(uinput, "KEY_" + key)
        self.emit(u_key, 1)

    def release_key(self, key):
        u_key = getattr(uinput, "KEY_" + key)
        self.emit(u_key, 0)

    def hold_key_for(self, key, time):
        # u_key = getattr(uinput, "KEY_" + key)
        self.emit(key, 1)
        sleep(time)
        self.emit(key, 0)

    def get_key_list(self):
        return self.key_list


"""
key = "H"
my_key = getattr(uinput,"KEY_"+key)
device.emit(my_key, 1) # Press.
device.emit(my_key, 0) # Release.

device = Gamepad([
        uinput.KEY_RIGHT,
        uinput.KEY_LEFT,
        uinput.KEY_UP,
        uinput.KEY_DOWN,
        uinput.KEY_RIGHTSHIFT,
        uinput.KEY_ENTER,
        ])
sleep(5)
"""
