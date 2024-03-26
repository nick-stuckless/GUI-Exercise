""" 
Description: 
  Graphical user interface that displays select information about a 
  user-specified Pokemon fetched from the PokeAPI 

Usage:
  python poke_info_viewer.py
"""
from tkinter import Tk, ttk
from poke_api import get_pokemon_info
# Create the main window
root = Tk()
root.title("Pokemon Information")

# Create the frames
input = ttk.Frame(root)
input.grid(row=0, column=0, columnspan=2, padx=(10,10), pady=(10,10))

info = ttk.LabelFrame(root, text="Info")
info.grid(row=1, column=0, sticky="N", padx=(5,10), pady=(5,10))

stats = ttk.LabelFrame(root, text="Stats")
stats.grid(row=1, column=1, sticky="N", padx=(5,10), pady=(5,10))

# Populate the user input frame with widgets
input_lbl = ttk.Label(input, text="Pokemon Name:")
input_lbl.grid(row=0, column=0)

input_ent = ttk.Entry(input)
input_ent.grid(row=0, column=1)

def get_info():
  poke_name = input_ent.get().strip()
  if not poke_name:
    return
  poke_info = get_pokemon_info(poke_name)
  if poke_info:
    height_val["text"] = poke_info["height"]
    weight_val["text"] = poke_info["weight"]
    #update type val

    hp_bar["value"] = poke_info["stats"][0]["base_stat"]
    attck_bar["value"] = poke_info["stats"][1]["base_stat"]
    def_bar["value"] = poke_info["stats"][2]["base_stat"]
    spec_attck_bar["value"] = poke_info["stats"][3]["base_stat"]
    spec_def_bar["value"] = poke_info["stats"][4]["base_stat"]
    speed_bar["value"] = poke_info["stats"][5]["base_stat"]
  else:
    pass #add error message
  return

input_but = ttk.Button(input, text="Get Info", command=get_info)
input_but.grid(row=0, column=2)


# Populate Info frame
height_lbl = ttk.Label(info, text="Height:")
weight_lbl = ttk.Label(info, text="Weight:")
type_lbl = ttk.Label(info, text="Type:")

height_lbl.grid(row=0, column=0, sticky="E", padx=(10,5), pady=(10,5))
weight_lbl.grid(row=1, column=0, sticky="E", padx=(10,5), pady=(10,5))
type_lbl.grid(row=2, column=0, sticky="E", padx=(10,5), pady=(5,10))

height_val = ttk.Label(info, width=20) #increases frame border
weight_val = ttk.Label(info)
type_val = ttk.Label(info)

height_val.grid(row=0, column=1, sticky="W", padx=(5,10), pady=(5,10))
weight_val.grid(row=1, column=1, sticky="W", padx=(5,10), pady=(5,10))
type_val.grid(row=2, column=1, sticky="W", padx=(5,10), pady=(10,5))

# Populate the Stats frame

hp_lbl = ttk.Label(stats, text="HP:")
attck_lbl = ttk.Label(stats, text="Attack:")
def_lbl = ttk.Label(stats, text="Defense:")
spec_attck_lbl = ttk.Label(stats, text="Special Attack:")
spec_def_lbl = ttk.Label(stats, text="Special Defense:")
speed_lbl = ttk.Label(stats, text="Speed:")

hp_lbl.grid(row=0, column=0, sticky="E", padx=(10,5), pady=(10,5))
attck_lbl.grid(row=1, column=0, sticky="E", padx=(10,5), pady=(10,5))
def_lbl.grid(row=2, column=0, sticky="E", padx=(10,5), pady=(10,5))
spec_attck_lbl.grid(row=3, column=0, sticky="E", padx=(10,5), pady=(10,5))
spec_def_lbl.grid(row=4, column=0, sticky="E", padx=(10,5), pady=(10,5))
speed_lbl.grid(row=5, column=0, sticky="E", padx=(10,5), pady=(5,10))

hp_bar = ttk.Progressbar(stats, maximum=255, length=200)
attck_bar = ttk.Progressbar(stats, maximum=255, length=200)
def_bar = ttk.Progressbar(stats, maximum=255, length=200)
spec_attck_bar = ttk.Progressbar(stats, maximum=255, length=200)
spec_def_bar = ttk.Progressbar(stats, maximum=255, length=200)
speed_bar = ttk.Progressbar(stats, maximum=255, length=200)

hp_bar.grid(row=0, column=1, padx=(5,10), pady=(5,10))
attck_bar.grid(row=1, column=1, padx=(5,10), pady=(5,10))
def_bar.grid(row=2, column=1, padx=(5,10), pady=(5,10))
spec_attck_bar.grid(row=3, column=1, padx=(5,10), pady=(5,10))
spec_def_bar.grid(row=4, column=1, padx=(5,10), pady=(5,10))
speed_bar.grid(row=5, column=1, padx=(5,10), pady=(10,5))

root.mainloop()