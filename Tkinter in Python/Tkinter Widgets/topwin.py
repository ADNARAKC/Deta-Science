from tkinter import *
window=Tk()
window.title("main")
window.geometry("400x300")

def topwin():
    top=Toplevel()
    top.geometry("180x100")
    top.title("Toplevel window")
    label=Label(top,text="This is a label on toplevel window")
    label.pack()
    top.mainloop()

l=Label(window, text='This is the main window')
btn=Button(window,text="Click here to open top window",command=topwin)
l.pack()
btn.pack()

window.mainloop()