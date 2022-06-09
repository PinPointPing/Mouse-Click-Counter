import os
import threading
import tkinter as tk
from pynput.mouse import Listener


clicks = 0

def on_click(x, y, button, pressed):
    global clicks, label
    if not pressed: return
    clicks += 1
    label["text"] = "{:,}".format(clicks)

def counter():
    with Listener(on_click=on_click) as listener: listener.join()
threading.Thread(daemon=True, target=counter).start()


root = tk.Tk()
root.geometry("400x100")
root.resizable(False, False)
root.title("Mouse Click Counter")

label = tk.Label(root, text=clicks, font=("", 60))
label.pack()

root.mainloop()