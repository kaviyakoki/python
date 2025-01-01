from tkinter import*
from tkinter import ttk
root=Tk()
root.title("open file")
root.geometry('500x400')
combo=ttk.Combobox(root,values=["name","age","qualify","place"])
combo.pack()
def option_selected(detail):
    selected_option=combo.get()
    print("you selected:",selected_option)
combo.bind("<<comboboxselected>>",option_selected)
root.mainloop()