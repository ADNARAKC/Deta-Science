from tkinter import *
from PIL import Image,ImageTk

win=Tk()
win.title("Adding image")
win.geometry('400x400')

upload=Image.open("cd.jpg")
image=ImageTk.PhotoImage(upload)

label=Label(win,image=image,height=35,width=200)
label.place(x=50,y=0)

label2=Label(win,text="Adding image")
label2.place(x=40,y=360)

win.mainloop()