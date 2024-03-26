""" 
Description: 
  Graphical user interface that displays select information about a 
  user-specified Pokemon fetched from the PokeAPI 

Usage:
  python poke_info_viewer.py
"""
from tkinter import Tk, ttk

# Create the main window
root = Tk()
root.title("Pokemon Information")

# Create the frames
input = ttk.Frame(root)
input.grid(row=0, column=0)

info = ttk.LabelFrame(root, text="Info")
info.grid(row=1, column=0)

stats = ttk.LabelFrame(root, text="Stats")
stats.grid(row=1, column=1)

# Populate the user input frame with widgets
input_lbl = ttk.Label(input, text="Pokemon Name:")
input_lbl.grid(row=0, column=0)

input_ent = ttk.Entry(input)
input_ent.grid(row=0, column=1)

input_but = ttk.Button(input, text="Get Info")
input_but.grid(row=0, column=2)

# Populate Info frame
height_lbl = ttk.Label(info, text="Height:")
weight_lbl = ttk.Label(info, text="Weight:")
type_lbl = ttk.Label(info, text="Type:")

height_lbl.grid(row=0, column=0)
weight_lbl.grid(row=1, column=0)
type_lbl.grid(row=2, column=0)

# TODO: Define button click event handler function

root.mainloop()