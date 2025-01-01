from tkinter import*
k=Tk()
k.geometry("500x400")
image=PhotoImage(Image.open("nazz.jpg"))
label=Label(k,image=image)
label.pack()
k.mainloop()
#f=open("newfil.txt","a")
from tkinter import*
from tkinter import ttk
plant=Tk()
plant.title("studend details")
plant.geometry('500x500')
combo=ttk.combobox(plant,values=["name","age","place"])
combo.pack()