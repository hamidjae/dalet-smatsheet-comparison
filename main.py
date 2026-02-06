from tkinter import *
from tkinter import ttk
from pathlib import Path
import csv

#Establishing the name of the file
CSV_FILE = Path("form.csv")

#Establishing the TTK skeleton
root = Tk()
root.title("Series Form")
style = ttk.Style()
style.configure("Long.TEntry", padding="5 10 5 20")
frm = ttk.Frame(root, padding=10)


#Series Form
ttk.Label(frm, text="Title").grid(column=0, row=0, sticky="w")
title_text = Text(frm, height=2, width=60)
title_text.grid(column=1, row=0)

ttk.Label(frm, text="Short Title (25 chars)").grid(column=0, row=1, sticky="w")
shortTitle_text = Text(frm, height=2, width=60, wrap="word")
shortTitle_text.grid(column=1, row=1)

ttk.Label(frm, text="Sort Title").grid(column=0, row=2, sticky="w")
sortTitle_text = Text(frm, height = 2, width=60)
sortTitle_text.grid(column = 1, row = 2)

ttk.Label(frm, text="Long (1000 chars)").grid(column=0, row=3, sticky="w")
long_text = Text(frm, width=60, height=11, wrap="word")
long_text.grid(column=1, row=3)

ttk.Label(frm, text="Medium (250 chars)").grid(column=0, row=4, sticky="w")
medium_text = Text(frm, width=60, height=5, wrap="word")
medium_text.grid(column=1, row=4)

ttk.Label(frm, text="Short (99 chars)").grid(column=0, row=5, sticky="w")
short_text = Text(frm, width=60, height=4, wrap="word")
short_text.grid(column=1, row=5)

ttk.Label(frm, text="XShort (60 chars)").grid(column=0, row=6, sticky="w")
XShort_text = Text(frm, width=60, height=3, wrap="word")
XShort_text.grid(column=1, row=6)

ttk.Label(frm, text="Tiny (40 chars)").grid(column=0, row=7, sticky="w")
tiny_text = Text(frm, width=60, height=2, wrap="word")
tiny_text.grid(column=1, row=7)

ttk.Label(frm, text="SEO Keywords").grid(column=0, row=8, sticky="w")
SEO_text = Text(frm, width=60, height=2, wrap="word")
SEO_text.grid(column=1, row=8)

frm.grid()
root.mainloop()