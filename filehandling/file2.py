#open("filehand.txt","x")
#f=open("filehand.txt","w")
#f.write("constant")
#f=open("filehand.txt","a")
#f.write("\nclass\tname")
#f=open("filehand.txt","r")
#a=f.read()
#print(a)
a="welcome"
b="python"
f=open("filehand.txt","r")
range=f.read().split("\n")
for x in range:
    demo=x.split("\t")
    if demo[0]==a and demo[1]==b:
        print("logging")
    else:
        print("not")