import tkinter
from tkinter import *
from tkinter import ttk,font
def login(s):
    s.destroy()
    s=Tk()
    s.geometry("1000x700")
    s.title("stu_login")
    frame=Frame(s,width=1500,height=50,bg="grey")
    frame.pack()
    Label_font=font.Font(s,weight="bold",family="Time New Roman",size=20)
    x=Label(frame,text="stu_log",font=Label_font)
    x.config(bg="grey",fg="purple")
    frame=Frame(s,width=500,height=400,bg="yellow")
    frame.place(relx=0.35,rely=0.3)
    Label_font=font.Font(s,weight="bold",family="Time New Roman",size=15)
    l=Label(frame,text="LOGIN",font=Label_font,bg="green")
    l.place(relx=0.47,rely=0.84)
    label_font=font.Font(s,weight="bold",family="Time New Roman",size=10)
    a=Label(frame,text="Name:",font=label_font,fg="orange")
    a.place(relx=0.38,rely=0.24)
    b=Label(frame,text="Age:",font=label_font,fg="orange")
    b.place(relx=0.38,rely=0.32)

    l1=Entry(frame)
    l1.place(relx=0.54,rely=0.25)
    l2=Entry(frame)
    l2.place(relx=0.54,rely=0.33)

    b=Button(frame,text="LOGIN",font=Label_font,bg="sky blue",command=lambda:file(l1.get(),l2.get(),s))
    b.place(relx=0.47,rely=0.82)
    frame.pack()
    s.mainloop()
def file(a,b,s):
    t=a+" "+b+" "+"\n"
    f=open("login.txt","a")
    f.write(t)
    if a=="kaviya":
       print("true")
       login(s)
    else:
      print("false")

def page():
    #Home page
    s=Tk() 
    s.geometry("1500x700")
    s.title("student")
    frame=Frame(s,width=1500,height=50,bg="orange")
    frame.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=25)
    x=Label(frame,text="student",font=label_font)
    x.configure(bg="blue",fg="black")
    x.place(relx=0.45,rely=0.1)
    label_font=font.Font(weight="bold",family="Time New Roman",size=20)
    b=Button(s,text="LOGIN",font=label_font,bg="purple",command=lambda:login(s))
    b.place(relx=0.40,rely=0.3)
    frame=Frame(s,width=1000,height=40)
    frame.pack()
    frame.place(relx=0.0,rely=0.94)
    s.mainloop()
page()    

