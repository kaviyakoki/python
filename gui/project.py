import tkinter
from tkinter import*
from tkinter import ttk,font
from PIL import ImageTk,Image
def cus_log(n):
    n.destroy()
    n=Tk()
    n.geometry("1500x1500")
    n.title("BANK")
    frame=Frame(n,width=1500,height=50,bg="lightblue")
    frame.pack()
    Label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    x=Label(frame,text="CITY UNION",font=Label_font)
    x.configure(bg="pink",fg="lightblue")
    x.place(relx=0.45,rely=0.1)
    frame=Frame(n,width=800,height=700)
    frame.place(relx=0.38,rely=0.20)


    img=ImageTk.PhotoImage(Image.open("image.jpg"))
    label=Label(frame,image=img)
    label.pack()


    
    Label_font=font.Font(n,weight="bold",family="Times New,Roman",size=18)
    l=Label(frame,text="CUSTOMER LOGIN",font=Label_font,bg="lightblue")
    l.place(relx=0.30,rely=0.10)

    q=font.Font(n,weight="bold",family="Times New Roman",size=12)
    l=Label(frame,text="USERNAME:",font=q,bg="pink")
    l.place(relx=0.30,rely=0.30)
    l=Label(frame,text="PASSWORD:",font=q,bg="pink")
    l.place(relx=0.30,rely=0.40)
   
    l1=Entry(frame)
    l1.place(relx=0.50,rely=0.30)
    l2=Entry(frame)
    l2.place(relx=0.50,rely=0.40)
    B=Button(frame,text="LOGIN",font=q,bg="grey",command=lambda:cus_reg(n))
    B.place(relx=0.30,rely=0.70)
    e=Button(frame,text="BACK",font=Label_font,bg="grey",command=lambda:cus_reg(n))
    e.place(relx=0.60,rely=0.70)

    
    n.mainloop()
    

def file(a,b,c,d,n):
        t=a+" "+b+" "+c+" "+d+" "+"\n"
        f=open("bank.txt","a")
        f.write(t)
def cus_reg(n):
    n.destroy()
    n=Tk()
    n.geometry("1500x1500")
    n.title("BANK")
    frame=Frame(n,width=1500,height=50,bg="lightblue")
    frame.pack()
    Label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    x=Label(frame,text="CITY UNION",font=Label_font)
    x.configure(bg="pink",fg="lightblue")
    x.place(relx=0.45,rely=0.1)
    

    frame=Frame(n,width=800,height=700)
    frame.place(relx=0.38,rely=0.20)
    img=ImageTk.PhotoImage(Image.open("image.jpg"))
    label=Label(frame,image=img)
    label.pack()


    
    Label_font=font.Font(n,weight="bold",family="Times New,Roman",size=18)
    l=Label(frame,text="CUSTOMER REGISTER",font=Label_font,bg="lightblue")
    l.place(relx=0.30,rely=0.10)

    q=font.Font(n,weight="bold",family="Times New Roman",size=12)
    l=Label(frame,text="NAME:",font=q,bg="pink")
    l.place(relx=0.30,rely=0.30)
    l=Label(frame,text="AGE:",font=q,bg="pink")
    l.place(relx=0.30,rely=0.40)
    l=Label(frame,text="PLACE:",font=q,bg="pink")
    l.place(relx=0.30,rely=0.50)
    l=Label(frame,text="MOB NO:",font=q,bg="pink")
    l.place(relx=0.30,rely=0.60)
   
    l1=Entry(frame)
    l1.place(relx=0.45,rely=0.30)
    l2=Entry(frame)
    l2.place(relx=0.45,rely=0.40)
    l3=Entry(frame)
    l3.place(relx=0.45,rely=0.50)
    l4=Entry(frame)
    l4.place(relx=0.45,rely=0.60)


    B=Button(frame,text="REGISTER",font=Label_font,bg="grey",command=lambda:file(l1.get(),l2.get(),l3.get(),l4.get(),n))
    B.place(relx=0.30,rely=0.70)
    d=Button(frame,text="BACK",font=Label_font,bg="grey",command=lambda:cus_log(n))
    d.place(relx=0.60,rely=0.70)
    frame=Frame(n,width=1500,height=50,bg="yellow")
    frame.pack()
    frame.place(relx=0.0,rely=0.94)
    Label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    x=Label(frame,text="CITY UNION",font=Label_font)
    x.configure(bg="lightblue",fg="pink")
    x.place(relx=0.38,rely=0.1)

    
    
    n.mainloop()  

def Home():
    #home page
    n=Tk()
    n.geometry("1500x1500")
    n.title("BANK")
    frame=Frame(n,width=1500,height=50,bg="lightblue")
    frame.pack()
    Label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    x=Label(frame,text="BANK",font=Label_font)
    x.config(bg="lightblue",fg="pink")
    x.place(relx=0.45,rely=0.1)
  

    frame=Frame(n,width=700,height=700)
    frame.place(relx=0.50,rely=0.20)
    img=ImageTk.PhotoImage(Image.open("image.jpg"))
    label=Label(frame,image=img)
    label.pack()


    Label_font=font.Font(weight="bold",family="Times New Roman",size=20)
    B=Button(n,text="CUSTOMER LOGIN",font=Label_font,bg="pink",command=lambda:cus_log(n))
    B.place(relx=0.2,rely=0.3)
    C=Button(n,text="CUSTOMER REGISTER",font=Label_font,bg="lightblue",command=lambda:cus_reg(n))
    C.place(relx=0.2,rely=0.5)
    


    
    
    n.mainloop()

Home()
    


    
    
    

    
     