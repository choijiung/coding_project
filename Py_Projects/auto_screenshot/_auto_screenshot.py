import time
import keyboard
from PIL import ImageGrab

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("screenshots\screenshot{}.png".format(curr_time))

keyboard.add_hotkey("F9", screenshot)
keyboard.wait("esc")