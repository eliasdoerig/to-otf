import fontforge
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# create the root window
root = tk.Tk()
root.title('TTF to OTF')
root.resizable(False, False)
root.geometry('300x150')


def select_file():
    filetypes = (
        ('truetype font', '*.ttf'),
        ('All files', '*.*')  
    )

    filenames = fd.askopenfilenames(
        title='Open a Font',
        initialdir='/',
        filetypes=filetypes)

    if not filenames:
        return
    else:
        for filename in filenames:
            otfname = filename.replace(".ttf", ".otf")
            font = fontforge.open(filename)
            font.generate(otfname)

# open button
open_button = ttk.Button(
    root,
    text='Open a Font',
    command=select_file
)

open_button.pack(expand=True)


# run the application
root.mainloop()