from tkinter import*
from tkinter import ttk
root=Tk()
root.title("workout")
root.geometry('500x500')
work=ttk.Combobox(root,values=["button1","button2"])
work.pack()
def button_selected(event):
    selected_button=work.get()
    print("you select:",selected_button)
    work.bind("<<Comboboxselected>>",button_selected)
    root.mainloop()


