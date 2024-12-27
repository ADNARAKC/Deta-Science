from tkinter import *
window=Tk()
window.title("MY first Tkinter")
window.geometry('300x300')
greetings=Label(text='Hello',bg='White',fg='Black')
button=Button(text="Click me",bg='Cyan',fg="Black")
entry=Entry(fg='Yellow',bg='Cyan',width='50')

greetings.pack()
button.pack()
entry.pack()

frame=Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
l1=Label(master=frame, text='Label')
l1.pack()

tb=Text(fg='Black',bg='Purple')
tb.pack()
window.mainloop()