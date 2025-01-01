from  tkinter import *
r=Tk()
r.geometry("400x400")
l1=Label(r,text="name")
l1.place(relx=1.10,rely=1.10)
l2=Label(r,text="age")
l2.place(relx=1.11,rely=1.10)

f1=Entry()
f1.grid(relx=110.,rely=1.2)
f2=Entry()
f2.grid(relx=1.2,rely=1.2)

def own():
    f=open("summa.txt","a")
    f.write("\n"+f1.get()+"\t"+f2.get())
    b1=Button(r,text="ok",command=lambda:own())
    b1.grid(relx=1.3,rely=1.3)
r.mainloop()
