import requests
import time
import win32clipboard as w
import win32con
import os
from pynput import keyboard
from pynput.keyboard import Key,Controller
with open('d:/sg.txt', 'r', encoding='utf-8')as f:
    sData = f.readlines()
def transString(string):
    x=int(len(string)/35)+199
    s=[]
    for i in range(x):
        s.append(string[35*i:35*i+35])
    s=[data for data in s if data]
    return(s)


def setText(aString):  # 写入剪切板
    s=transString(aString)
    print(s)
    try:
        for aString in s:
            aString=aString.encode('utf-8')
            w.OpenClipboard()
            w.EmptyClipboard()
            w.SetClipboardData(win32con.CF_TEXT, aString)
            w.CloseClipboard()
            keyboard = Controller()
            # keyboard.press(Key.alt_l)
            keyboard.press(Key.enter)
            time.sleep(0.3)
            # keyboard.release(Key.alt_l)
            keyboard.release(Key.enter)
            time.sleep(0.3)
            keyboard.press(Key.ctrl_l)
            keyboard.press('v')
            time.sleep(0.3)
            keyboard.release('v')
            keyboard.release(Key.ctrl_l)
            time.sleep(0.3)
            # keyboard.press(Key.alt_l)
            keyboard.press(Key.enter)
            time.sleep(0.3)
            # keyboard.release(Key.alt_l)
            keyboard.release(Key.enter)
            print(1)
    except:
        pass

g_stopSignal=False

def on_press1(key):
    global g_stopSignal

    try:
        if key.char == '8' :
            # global g_stopSignal
            g_stopSignal = False
            while True:
                if g_stopSignal: break
                text = requests.get('https://nmsl.shadiao.app/api.php?lang=zh_cn').text
                print(text)

                setText(text)
        elif key.char == '7' :
            # global g_stopSignal
            g_stopSignal = False
            for data in sData:
                if g_stopSignal: break
                text =data
                setText(text)
    except:
        pass

def on_press2(key):
    try:
        if key.char == '9':
            global g_stopSignal
            g_stopSignal=True
    except:
        pass

def on_release(key):
    try:
        if key.char=='0':
            pid=os.getpid()
            os.system('taskkill /pid ' + str(pid) + ' /f')
            return False
    except:pass

def do():

    while True:
        listener1 = keyboard.Listener(on_press=on_press1, on_release=on_release)
        listener2 = keyboard.Listener(on_press=on_press2, on_release=on_release)
        listener1.start()
        listener2.start()
        print('ready')
        listener1.join()
        listener2.join()

do()
