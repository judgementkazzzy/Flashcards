# python 3.10.4

import tkinter as tk
from tkinter import *
#import datetime as dt

root = tk.Tk()
root.title('flashcards')
root.geometry('800x600')
root.columnconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

#category
#categories - list/ drop down
categories = ["Python", "C#", "C/C++", "Misc"] #ad nausem
categorybox = StringVar(root)
categorybox.set(categories[0]) # default value

#categories - dimensions
categorylist = OptionMenu(root, categorybox, *categories)
categorylist.grid(row=1, column=0, sticky=tk.E + tk.W)

#name
def temp_text(e):
   textbox.delete(0,"end")

textbox = Entry(root)
textbox.insert(0, "Name of project...")
textbox.grid(row=1, column=1, sticky=tk.E + tk.W)

textbox.bind("<FocusIn>", temp_text)

#entry / the actual meat of the text
mainEntry = tk.Text(root)
mainEntry.grid(row=2, column=0, columnspan=2, sticky='nesw')

#banner
banner = tk.Label(root, text='')
banner.grid(row=100, column=0, columnspan=2)

#saving as a csv
#saving - save button
save_btn = tk.Button(root, text='Save')
save_btn.grid(row=99, column=0, sticky=tk.W)

def save():
    # tried to include the date but was being a pain and didnt work 
    # atm = dt.datetime.now()
    # currentdate = atm.strftime("%x")
    # str_currenrdate = str(currentdate)

    categories = categorybox.get()
    name = textbox.get()

    message = mainEntry.get('1.0', tk.END)

    filename = f"{categories}_{name}.txt"
    with open(filename, "w") as fh:
        fh.write(message)

    banner.configure(text='File saved')

save_btn.configure(command=save)

root.mainloop()