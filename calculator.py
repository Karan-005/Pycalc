from _tkinter import *
# from audioop import add
from cProfile import label
from calendar import c
# from cgitb import text
from multiprocessing import Value
from re import X
from tkinter import LEFT, W, Button, Entry, Frame, IntVar, Place, StringVar, Tk, Widget
import tkinter
from turtle import clear, width
from webbrowser import get
import tkinter as tk

# def Click1(event):
#     global svalue
#     text = event.widget.cget("text") 
#     print(text)
#     if text == "=":
#         pass
#     elif text == "C":
#         pass
#     else:
#         svalue.set(svalue.get() + text)
#         E.update()
    

root = Tk()
root.geometry("300x350")
root.title("Calculator by CodewithKaran")
root.resizable(False, False)


def show(value):
    current_text = E.get()
    E.delete(0, tk.END)
    E.insert(tk.END, current_text + str(value))
    
    
def clear():
    
    E.delete(0, tk.END)

def solve(): 
    try:   
        result = eval(E.get())
        E.delete(0, tk.END)
        E.insert(tk.END, str(result))
    except Exception as e:
        E.delete(0, tk.END)
        E.insert(tk.END, "Error")
        

svalue = StringVar()
entry_value= ""
svalue.set("")

E = Entry(root, textvariable=svalue, font="lucida 30 bold",bg="black",fg="white" )
E.pack(padx=5, pady=8, ipadx=8, fill="x")



b1 = Button(root, text="9", font="lucida 25 bold" , width=3, bg="white",command=lambda:show(9)).place(x=10 ,y=70)
b2 = Button(root, text="8", font="lucida 25 bold" , width=3, bg="white", command=lambda: show(8)).place(x=80 ,y=70)

b3 = Button(root, text="7", font="lucida 25 bold" , width=3, bg="white", command=lambda:show(7)).place(x=150 ,y=70)
b4 = Button(root, text="C", font="lucida 25 bold" , width=3, bg="yellow",command=clear).place(x=220 ,y=70)

# Second Row

b5 = Button(root, text="6", font="lucida 25 bold" , width=3, bg="white",command=lambda:show(6)).place(x=10 ,y=140)
b6 = Button(root, text="5", font="lucida 25 bold" , width=3, bg="white",command=lambda:show(5)).place(x=80 ,y=140)
b7 = Button(root, text="4", font="lucida 25 bold" , width=3, bg="white",command=lambda:show(4)).place(x=150 ,y=140)
b8 = Button(root, text="/", font="lucida 25 bold" , width=3, bg="grey",command=lambda:show("/")).place(x=220 ,y=140)

# Third Row

b9 = Button(root, text="3", font="lucida 25 bold" , width=3, bg="white",command=lambda:show(3)).place(x=10 ,y=210)
b10 = Button(root, text="2", font="lucida 25 bold" , width=3, bg="white",command=lambda:show(2)).place(x=80 ,y=210)
b11 = Button(root, text="1", font="lucida 25 bold" , width=3, bg="white",command=lambda:show(1)).place(x=150 ,y=210)
b12 = Button(root, text="+", font="lucida 25 bold" , width=3, bg="grey",command=lambda:show("+")).place(x=220 ,y=210)

# forth row

b13 = Button(root, text="*", font="lucida 25 bold" , width=3, bg="grey",command=lambda:show("*")).place(x=10 ,y=280)
b14 = Button(root, text="-", font="lucida 25 bold" , width=3, bg="grey",command=lambda:show("-")).place(x=80 ,y=280)
# b15 = Button(root, text="", font="lucida 25 bold" , width=3, bg="grey",command=lambda:show(())).place(x=150 ,y=280)
b16 = Button(root, text="=", font="lucida 25 bold" , width=6, height=1 ,bg="grey",command=solve, padx=6).place(x=150,y=280)





root.mainloop()