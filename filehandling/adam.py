import tkinter 
from tkinter import *
from tkinter import ttk,font 


def ad_no(k):
    k.destroy()
    k=Tk()
    k.geometry("1000x700")
    k.title("adam")
    frame=Frame(k,width=1500,height=50,bg="light green")
    frame.pack()
    Label_font=font.Font(k,weight="bold",family="Time New Roman",size=20)
    x=Label(frame,text="addum",font=Label_font)
    x.config(bg="purple",fg="green")
    frame=Frame(s,width=500,height=400,bg="purple")
    frame.place(relx=0.35,rely=0.3)
    label_font=font.Font(k,weight="bold",family="Time New Roman",size=10)
    l=Label(frame,text="ad num:",font=label_font,fg="purple")
    l.place(relx=0.38,rely=0.24)
    l1=Entry(frame)
    l1.place(relx=0.54,rely=0.25)    
    b=Button(frame,text="submit",font=Label_font,bg="green",command=lambda:file(l1.get(),k))
    b.place(relx=0.47,rely=0.82)
    frame.pack()
    k.mainloop()
def file(a,k):
   t=a+" "+k+" "+"\n"
   f=open("adam.text","a")
   f.write(t)
     



    
   
   

n1=n=int(input("Enter the value:"))
a=n*n

r=0
while a>0:
    c=a%10
    r=(r*10)+c
    a//=10

s=r
r=0
while n>0:
    c=n%10
    r=(r*10)+c
    n//=10

b=r*r

if(s==b):
        print("adam number")
        if(n1%2):
              print("addum")
        else:
             print("odd")
else:
     print("not adam number")
def file(k):
    
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
    b=Button(k,text="submit",font=label_font,bg="pink",command=lambda:file(a,k))
    b.place(relx=0.40,rely=0.3)
    frame=Frame(k,width=1000,height=40)
    frame.pack()
    frame.place(relx=0.0,rely=0.94)
    k.mainloop()

#page()
