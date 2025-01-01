import tkinter 
from tkinter import*
from tkinter import ttk,font
def reg(k):
    k.destroy()
    k=Tk()
    k.geometry("1000X700")
    k.title("Register")
    frame=Frame(k,width=1000,height=30,bg="green")
    frame.pack()
    label_font=font.Font(k,weight="bold",family="Times New Roman",size=10)
    x=Label(frame,text="Login",font=label_font)
    x.config(bg="purple",fg="yellow")
    frame=Frame(k,weight=500,height=500,bg="blue")
    frame.place(relx=0.35,rely=0.3)

    label_font=font.Font(k,weight="bold",family="Times New Roman",size=15)
    l=Label(frame,text="User Name",font=label_font,bg="pink")
    l.place(relx=0.40,rely=0.1)
    label_font=font.Font(k,weight="bold",family="Times New Roman",size=15)
    l=Label(frame,text="Password",font=label_font,bg="pink")
    l.place(relx=0.45,rely=0.4)
    l=Label(frame,text="Name",font=label_font,bg="orange")
    l.place(relx=0.45,rely=0.11)
    l=Label(frame,tex="Age",font=label_font,bg="pink")
    l.place(relx=0.45,rely=16)
    l1=Entry(frame)
    l1.place(relx=0.45,rely=0.41)
    l2=Entry(frame)
    l2.place(relx=0.45,rely=0.41)
    b=Button(frame,text="LOGIN",font=label_font,bg="orange",command=lambda:(l1.get(),l2.get(),k))
    b.place(relx=0.61,rely=0.7)
    frame=Frame(k,width=1500,height=50,bg="grey")
    frame.place(relx=0.0,rely=0.94)
    frame.pack()
    k.mainloop()

      

def file(a,b,k):
    t=a+" "+b+" "+k+" "+"\n"
    f=open("BANK.text","a")
    f.write(t)
    
