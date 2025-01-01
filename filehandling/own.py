from  tkinter import *
r=Tk()
r.geometry("400x400")
l1=Label(r,text="name")
l1.place(relx=0.0,rely=0.1)
l2=Label(r,text="age")
l2.place(relx=0.10,rely=0.1)

e1=Entry()
e1.place(relx=0.0,rely=0.2)
e2=Entry()
e2.place(relx=0.10,rely=0.2)
def own():
    f=open("summa.txt","a")
    f.write("\n"+e1.get()+"\n"+e2.get())
    b1=Button(r,text="ok",command=lambda:own())
    b1.place(relx=0.0,rely=0.3)
r.mainloop()
