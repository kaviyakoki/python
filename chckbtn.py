'''
from tkinter import*
r=Tk()
n=IntVar()
c=Checkbutton(r,text="file1").pack()
c1=Checkbutton(r,text="file2").pack()
c2=Checkbutton(r,text="file3").pack()
r.mainloop()
'''
from tkinter import*
n=Tk()
m=IntVar()
a=Checkbutton(n,text="folder1").pack()
b=Checkbutton(n,text="folder2").pack()
c=Checkbutton(n,text="folder3").pack()
n.mainloop()
              