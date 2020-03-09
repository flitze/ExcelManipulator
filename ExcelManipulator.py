import pandas as pd
from tkinter import *
from tkinter import filedialog


print("test")

options = ["Test"]

root = Tk()


def open():
    global options
    global clicked
    root.filename = filedialog.askopenfilename(initialdir="C:\ProgrammierungGIT\ExcelManipulator"
                                              , title="Select A File"
                                              , filetypes=(("Excel Files", "*.xlsx"), ("CSV Files", "*.csv"),))
    my_label = Label(root, text=root.filename).pack()
    test_excel = pd.read_excel(root.filename)
    print(test_excel.head())
    options = list(test_excel.columns.values)
    clicked.set(options)
    
clicked = StringVar()
  

drop = OptionMenu(root, clicked, *options)
drop.pack()
my_btn = Button(root, text="Read Spreasheet", command=open).pack()
my_btn_2 = Button(root, text="Read Spreasheet 2", command=open).pack()


root.mainloop()