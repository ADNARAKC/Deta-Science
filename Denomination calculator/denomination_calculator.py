from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root =Tk()
root.title("Denomination Calculator")
root.configure(bg="Cyan")
root.geometry("650x400")

upload=Image.open("de.png")
upload=upload.resize((300,300))

image= ImageTk.PhotoImage(upload)

label=Label(root,image=image, bg="Green")
label.place(x=180,y=20)
label1=Label(root, text="Welcome to denomination calculator app", bg="Blue")
label1.place(relx=0.5,y=340, anchor=CENTER)

def msg():
    msg_box=messagebox.showinfo("Alert","Do you want to calculate?")
    if msg_box=='ok':
        topwin()

button1=Button(root, text="lets get started", command=msg, bg='Black',fg="White")
button1.place(x=260,y=360)

def topwin():
    top=Toplevel()
    top.title('denomination window')
    top.configure(bg="Light grey")
    top.geometry("600x450")

    label=Label(top, text="Enter the amount", bg="Dark green")
    entry=Entry(top)

    label1=Label(top,text="Here are the numbers for denominations",bg="Dark blue")

    l1=Label(top,text="500",bg="Purple")
    l2=Label(top,text="100",bg="Purple")
    l3=Label(top,text="50",bg="Purple")

    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)

    def calculator():
        try: 
            global amount
            amount=int(entry.get())

            note500=amount//500
            amount %=500
            note100=amount//100
            amount %=100
            note50=amount//50
            amount %=50

            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)

            t1.insert(END,str(note500))
            t2.insert(END,str(note100))
            t3.insert(END,str(note50))
        except ValueError:
            messagebox.showerror("Error","Invalid Input!! Please enter a valid input.")
    btn=Button(top,text="Calculate",command=calculator, bg="Brown", fg="White")

    label.place(x=230,y=50)
    entry.place(x=200,y=80)
    btn.place(x=240,y=120)
    label1.place(x=140,y=170)

    l1.place(x=180,y=200)
    l2.place(x=180,y=230)
    l3.place(x=180,y=250)

    t1.place(x=270,y=200)
    t2.place(x=270,y=230)
    t3.place(x=270,y=260)

    top.mainloop()
root.mainloop()