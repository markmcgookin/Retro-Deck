import time

from adafruit_hid.keycode import Keycode

###
# Debug buttons functions
# Methods for the debug profile of the RetroDeck
###

class DevopsButtonFunctions:
    mode = 'Devops'

    def print_name(self, name):
        print(name)
        self.screen.set_confirm_selection(self.mode, name)
        
    # define methods for starting the project and stopping the project
    def kill_builds(self, button_index):
        self.print_name('Kill All')
        self.kbd.press(Keycode.CONTROL)
        self.kbd.press(Keycode.SHIFT)
        self.kbd.press(Keycode.COMMAND)
        self.kbd.press(Keycode.ONE)
        time.sleep(0.1)
        self.kbd.release_all()
        time.sleep(1.5)

    def build_core(self, button_index):
        self.print_name('Core API')
        self.kbd.press(Keycode.CONTROL)
        self.kbd.press(Keycode.SHIFT)
        self.kbd.press(Keycode.COMMAND)
        self.kbd.press(Keycode.TWO)
        time.sleep(0.1)
        self.kbd.release_all()
        time.sleep(1.5)

    def build_query(self, button_index):
        self.print_name('Query API')
        self.kbd.press(Keycode.CONTROL)
        self.kbd.press(Keycode.SHIFT)
        self.kbd.press(Keycode.COMMAND)
        self.kbd.press(Keycode.THREE)
        time.sleep(0.1)
        self.kbd.release_all()
        time.sleep(1.5)

    def build_document(self, button_index):
        self.print_name('Doc API')
        self.kbd.press(Keycode.CONTROL)
        self.kbd.press(Keycode.SHIFT)
        self.kbd.press(Keycode.COMMAND)
        self.kbd.press(Keycode.FOUR)
        time.sleep(0.1)
        self.kbd.release_all()
        time.sleep(1.5)

    def build_worker(self, button_index):
        self.print_name('Workers')
        self.kbd.press(Keycode.CONTROL)
        self.kbd.press(Keycode.SHIFT)
        self.kbd.press(Keycode.COMMAND)
        self.kbd.press(Keycode.FIVE)
        time.sleep(0.1)
        self.kbd.release_all()
        time.sleep(1.5)

    def build_signal(self, button_index):
        self.print_name('SignalR')
        self.kbd.press(Keycode.CONTROL)
        self.kbd.press(Keycode.SHIFT)
        self.kbd.press(Keycode.COMMAND)
        self.kbd.press(Keycode.SIX)
        time.sleep(0.1)
        self.kbd.release_all()
        time.sleep(1.5)

    def __init__(self, screen, kbd):
        self.screen = screen
        self.kbd = kbd
        self.config = {
            1: {
                'name': 'Kill Builds',
                'action': self.kill_builds
            },
            2: {
                'name': 'Build Core',
                'action': self.build_core
            },
            3: {
                'name': 'Build Query',
                'action': self.build_query
            },
            4: {
                'name': 'Build Document',
                'action': self.build_document
            },
            5: {
                'name': 'Build Workers',
                'action': self.build_worker
            },
            6: {
                'name': 'Build SignalR',
                'action': self.build_signal
            },
            7: {
                'name': 'BTN 7',
                'action': self.print_name
            },
            8: {
                'name': 'BTN 8',
                'action': self.print_name
            }
        }
