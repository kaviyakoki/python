#open("view.txt","x")
#f=open("view.txt","w")
#f.write("python")
#f=open("view.txt","a")
#f.write("\nclass\tage")
#f=open("view.txt","r")
#a=f.read()
#print(a)
a="class"
b="age"
f=open("view.txt","r")
range=f.read().split("\n")
for x in range:
    username=x.split("\t")
    if username[0]==a and username[0]==b:
        print("logging")
    else:
        print("not")
