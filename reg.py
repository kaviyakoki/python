from tkinter import*
r=Tk()
r.geometry("500x500")
l0=Label(r,text="REGISTER FORM",bg="pink")
l0.place(relx=0.50,rely=0.0)
l1=Label(r,text="Name")
l1.place(relx=0.1,rely=0.2)
l2=Label(r,text="Age")
l2.place(relx=0.1,rely=0.3)
l3=Label(r,text="Reg no")
l3.place(relx=0.1,rely=0.4)
l4=Label(r,text="Mob no")
l4.place(relx=0.1,rely=0.5)

s1=Entry(r)
s1.place(relx=0.2,rely=0.2)
s2=Entry(r)
s2.place(relx=0.2,rely=0.3)
s3=Entry(r)
s3.place(relx=0.2,rely=0.4)
s4=Entry(r)
s4.place(relx=0.2,rely=0.5)

b=Button(r,text="Submit")
b.place(relx=0.3,rely=0.6)
r.mainloop()