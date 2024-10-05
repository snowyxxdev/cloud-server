# server

import os
import random
import threading
import string
from tkinter import messagebox
import time
import ctypes

alphanumerical=list(string.ascii_letters+string.digits)
var = ''.join(random.choice(alphanumerical) for _ in range(50))
os.system("mode con: cols=100 lines=30")
os.system("cls" if os.name == "nt" else "clear")
os.system(f"title {var}")
x=True

""" main """

def tempfunc():
    while(x):
        os.system("color fc")
        os.system("color 08")

def tempfuncc():
    while(x):
        os.system("color fc")
        os.system("color 08")

def change_pos():
    while(x):
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        xs = random.randint(1, 1000)
        ys = random.randint(1, 1000)
        ctypes.windll.user32.SetWindowPos(hwnd, None, xs, ys, 0, 0, 0x0001)

def popup():
    messagebox.showerror(var, "404 | CONGRATULATIONS YOU'VE BEEN HACKED | 404")


threading.Thread(target=popup).start()
threading.Thread(target=tempfunc).start()
threading.Thread(target=tempfuncc).start()
threading.Thread(target=change_pos).start()
