open("file3.txt")
a=str(input("enter a name:"))
b=int(input("enter a age:"))
def my_function():
    open("file3.txt","x")
    f=open("file3.txt","a")
    f.write("\n"+a.get()+"\n"+b.get())
    a=("a.get()")
    b=("b.get()")