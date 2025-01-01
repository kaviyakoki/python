from tkinter import*
from PIL import Image
from PIL.ImageTk import PhotoImage
k=Tk()
k.geometry("500x400")
img=PhotoImage(Image.open("nazz.jpg"))
label=Label(k,image=img)
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