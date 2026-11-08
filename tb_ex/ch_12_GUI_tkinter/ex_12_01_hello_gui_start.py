# file: ex_12_01_hello_gui_start.py
import tkinter as tk
from tkinter import ttk

# TODO: Create the main window with tk.Tk()
#       Set a title with root.title()
#       Set a minimum size with root.minsize()
root = tk.Tk()
root.title("Sakineh`s første GUI")
root.minsize(300, 100)
# TODO: Add a ttk.Label with a greeting message
#       Pack it with some padding
label = ttk.Label(root, text="Hei, dette er min første GUI-program")
label.pack(padx=20, pady=10)
# TODO: Keep a click counter (use a list [0] or a global variable)
counter = [0]
# TODO: Write a callback function on_click() that:
#         - increments the counter
#         - updates the label text
def on_click():
    counter[0] += 1
    label.config(text=f"Antall klikk: {str(counter[0])}")
# TODO: Add a ttk.Button labelled "Click me!" connected to on_click
button = ttk.Button(root, text="Click me", command=on_click)
button.pack(padx=10, pady=10)
# TODO: Start the event loop with root.mainloop()
root.mainloop()