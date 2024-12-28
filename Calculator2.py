from cgitb import text
from ctypes import pointer
from logging import root
from msilib.schema import File
import os
from sqlite3 import Cursor
from tkinter import *
from tkinter import filedialog
from turtle import dot, right
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfile, asksaveasfilename

from django.forms import Textarea 

root = Tk()
root.title("Notepad")
root.geometry("456x457")

TextArea = Text(root, font="lucida 12")
file = None
TextArea.pack(fill=BOTH, expand=TRUE)

def new():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def save():
    global file
    if file == None:

      file = asksaveasfilename(initialfile="untitled.txt", defaultextension=".txt",
                               filetypes=[("All files","*.*"), ("Text Document", "*.txt")])
      
      if file == "":
          file = None
      else:
          #save as a new file 
          f= open(file,"w")
          f.write(TextArea.get(1.0, END))
          f.close()  

          root.title(os.path.basename(file) + "- NotePad ") 
    else:
         #save a file
         f= open(file,"w")
         f.write(TextArea.get(1.0, END))
         f.close()  






def Open():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All files","*.*"), ("Text Document", "*.txt")])
    if file == "":
        file =None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()    


def Paste():
    TextArea.event_generate(("<<Paste>>"))
def Cut():
    TextArea.event_generate(("<<Cut>>"))
def Copy():
    TextArea.event_generate(("<<Copy>>"))

def Exit():
    root.destroy()    

def About():
    tmsg.showinfo("Info!!", "This is presented by Karancoding..")

# *******************************




menubar = Menu(root,)
filemenu = Menu(menubar, tearoff=0)
#   to create files
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=Open)
filemenu.add_separator()
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="Files", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Copy", command=Copy)
editmenu.add_command(label="Cut", command=Cut)
editmenu.add_command(label="Paste", command=Paste)
menubar.add_cascade(label="Edit", menu=editmenu)

aboutmenu = Menu(menubar, tearoff=0)
aboutmenu.add_command(label="About", command=About)
menubar.add_cascade(label="About", menu=aboutmenu)



root.config(menu=menubar)

scroll = Scrollbar(TextArea, cursor="arrow", bg="yellow")
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=scroll.set)



root.mainloop()
