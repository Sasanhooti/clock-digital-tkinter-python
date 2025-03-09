import sqlite3
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

window = Tk()
window.title('دفترچه تلفن')
window.geometry('450x400')
window.resizable(0,0)

Mid = Frame(window, width=500,  bg="red")
Mid.pack(side=TOP)
MidLeft = Frame(Mid, width=100)
MidLeft.pack(side=LEFT, pady=10)
MidLeftPadding = Frame(Mid, width=200)
MidLeftPadding.pack(side=LEFT)
MidRight = Frame(Mid, width=100)
MidRight.pack(side=RIGHT, pady=10)

btn_add = Button(MidRight, text="+ اضافه کردن", bg="pink",foreground="black")
btn_add.pack(side=RIGHT)

btn_delete = Button(MidLeft, text="- حذف کردن", bg="pink",foreground="black")
btn_delete.pack(side=LEFT)

Mid = Frame(window, width=500,  bg="red")
Mid.pack(side=TOP)
MidLeft = Frame(Mid, width=100)
MidLeft.pack(side=LEFT, pady=10)
MidLeftPadding = Frame(Mid, width=200)
MidLeftPadding.pack(side=LEFT)
MidRight = Frame(Mid, width=100)
MidRight.pack(side=RIGHT, pady=10)

btn_add = Button(MidRight, text="+ اضافه کردن", bg="pink",foreground="black")
btn_add.pack(side=RIGHT)

btn_delete = Button(MidLeft, text="- حذف کردن", bg="pink",foreground="black")
btn_delete.pack(side=LEFT)