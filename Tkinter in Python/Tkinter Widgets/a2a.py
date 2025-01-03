from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Adding messagebox")
window.geometry("200x200")

def msg():
    messagebox.showwarning("Alert",'Stop! virus found')

button=Button(window,text='Scan for virus',command=msg)
button.place(x=40,y=80)

window.mainloop()