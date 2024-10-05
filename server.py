# server

import os

try:
    from tkinter import messagebox
except Exception:
    os.system("python -m pip install tkinter")
from tkinter import messagebox

""" main """

messagebox.showinfo("Success!", "You've connected to SnowyCloud's servers.")
