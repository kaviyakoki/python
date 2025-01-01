import tkinter 
from tkinter import *
from tkinter import ttk,font 


def stu_log(k):
    k.destroy()
    k=Tk()
    k.geometry("1000x700")
    k.title("student")
    frame=Frame(k,width=1500,height=50,bg="blue")
    frame.pack()
    Label_font=font.Font(k,weight="bold",family="Time New Roman",size=20)
    x=Label(frame,text="stu_log",font=Label_font)
    x.config(bg="yellow",fg="purple")
    frame=Frame(k,width=500,height=400,bg="orange")
    frame.place(relx=0.35,rely=0.3)
    Label_font=font.Font(k,weight="bold",family="Time New Roman",size=15)
    l=Label(frame,text="submit",font=Label_font,bg="green")
    l.place(relx=0.47,rely=0.84)
    label_font=font.Font(k,weight="bold",family="Time New Roman",size=10)
    l=Label(frame,text="Name:",font=label_font,fg="green")
    l.place(relx=0.38,rely=0.24)
    l=Label(frame,text="Age:",font=label_font,fg="green")
    l.place(relx=0.38,rely=0.32)
    l=Label(frame,text="email:",font=label_font,fg="green")
    l.place(relx=0.38,rely=0.40)
    l=Label(frame,text="mark1:",font=label_font,fg="green")
    l.place(relx=0.38,rely=0.48)
    l=Label(frame,text="mark2:",font=Label_font,fg="green")
    l.place(relx=0.38,rely=0.56)
    l1=Entry(frame)
    l1.place(relx=0.54,rely=0.25)
    l2=Entry(frame)
    l2.place(relx=0.54,rely=0.33)
    l3=Entry(frame)
    l3.place(relx=0.54,rely=0.41)
    l4=Entry(frame)
    l4.place(relx=0.54,rely=0.49)
    l5=Entry(frame)
    l5.place(relx=0.54,rely=0.57)

    b=Button(frame,text="submit",font=Label_font,bg="pink",command=lambda:file(l1.get(),l2.get(),l3.get(),l4.get(),l5.get(),k))
    b.place(relx=0.47,rely=0.82)
    frame.pack()
    k.mainloop()
def file(a,b,c,d,e,k):
    t=a+" "+b+" "+c+" "+d+" "+e+" "+"\n"
    f=open("student.txt","a")
    f.write(t)



def page():
    
    #Home page
    k=Tk() 
    k.geometry("1500x700")
    k.title("student")
    frame=Frame(k,width=1500,height=50,bg="orange")
    frame.pack()
    label_font=font.Font(weight="bold",family="Times New Roman",size=25)
    x=Label(frame,text="student",font=label_font)
    x.configure(bg="orange",fg="black")
    x.place(relx=0.45,rely=0.1)
    label_font=font.Font(weight="bold",family="Time New Roman",size=20)
    b=Button(k,text="submit",font=label_font,bg="pink",command=lambda:stu_log(k))
    b.place(relx=0.40,rely=0.3)
    frame=Frame(k,width=1000,height=40)
    frame.pack()
    frame.place(relx=0.0,rely=0.94)
    k.mainloop()
page()    
