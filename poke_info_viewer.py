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

# TODO: Create the frames
input = ttk.Frame(root)
input.grid(row=0, column=0)

info = ttk.LabelFrame(root, text="Info")
info.grid(row=1, column=0)

stats = ttk.LabelFrame(root, text="Stats")
stats.grid(row=1, column=1)

# TODO: Populate the user input frame with widgets

# TODO: Define button click event handler function

root.mainloop()