import tkinter
from tkinter import *
from tkinter import ttk,font
def login(k):
    
    k=Tk()
    k.geometry("1000X700")
    k.title("Login")
    frame=Frame(k,width=1500,height=50,bg="blue")
    frame.pack()
    Label=font.Font(k,weight="bold",family='Times New Roman',size=20)
    x=Label(frame,text="claim",font=Label)
    x.config(bg="yellow",fg="purple")
    a1=Label(frame,text="username",font=Label,fg="purple")
    a1.place(relx=0.38,rely=0.24)
    a2=Label(frame,text="password",font=Label,fg="purple")
    a2.place(relx=0.38,rely=0.24)
    l=Entry(frame)
    l.place(relx=0.20,rely=0.5)
    l2=Entry(frame)
    l2.place(relx=0.25,rely=0.5)
    label=font.Font(k,weight="bold",family="Times New Roman",size=20)
    x=Label(frame,text="Login",font=label)
    x.config(bg="pink",fg="sky blue")
    frame=Frame(k,width="500",height="400",bg="yellow")
    frame.place(relx=0.35,rely=0.3)
    k.place(relx=0.38,rely=0.24)
    l=Label(frame,text="LOGIN",font=Label,bg="green")
    l.place(relx=0.47,rely=0.84)
    a=Label(frame,text="Name",font=Label,fg="green")
    a.place(relx=0.38,rely=0.24)
    b=Label(frame,text="Age",font=Label,fg="green")
    b.place(relx=0.38,rely=32)
    c=Label(frame,text="Contact no",fg="green")
    c.place(relx=0.38,rely=0.40)
    d=Label(frame,text="Email",font=Label,fg="green")
    d.place(relx=0.38,rely=0.48)
    l1=Entry(frame)
    l1.place(relx=0.54,rely=0.25)
    l2=Entry(frame)
    l2.place(relx=0.54,rely=0.25)
    l3=Entry(frame)
    l3.place(relx=0.54,rely=0.25)
    l4=Entry(frame)
    l4.place(relx=0.54,rely=0.25)
    b=Button(frame,text="LOGIN",font=Label,bg="sky blue",command=lambda:(l1.get(),l2.get(),l3.get(),l4.get(),k))
    b.place(relx=0.47,rely=0.82)
    frame.pack()
    k.mainloop()
    


        
        


    