from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.title('project')
root.geometry('400x400')

l1=Label(root,text="Hello!",bg='black',fg='white')
e1=Entry(root)
b1=Button(root,text="Click me",bg='brown',fg='white')
upload=Image.open('png-transparent-blue-and-yellow-logo-python-logo-programmer-fierce-python-s-cdr-angle-text-thumbnail.png')
upload=upload.resize('50x50')
i1=ImageTk.PhotoImage(upload)
l2=Label(root,image=i1)

l1.place(x=50,y=50)
e1.place(x=50,y=100)
b1.place(x=50,y=130)
l2.place(x=50,y=200)

root.mainloop()