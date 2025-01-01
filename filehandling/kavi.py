#open("workout.txt","x")
#f=open("workout.txt","w")
#f.write("new")
#f=open("workout.txt","a")
#f.write("\nname\tage")
#f=open("workout.txt","r")
#a=f.read()
#print(a)
a="name"
b="age"
f=open("workout.txt","r")
lines=f.read().split("\n")
a=input("enter a name:")
b=int(input("enter a age:"))
m1=int(input("enter a mark:"))
m2=int(input("enter a mark:"))
m3=int(input("enter a mark:"))
m4=int(input("enter a mark:"))
m5=int(input("enter a mark:"))
total=m1+m2+m3+m4+m5
print(total)
average=total/5
print(average)
if average<=60:
    print("arts")
elif average<=70:
    print("engineer")
elif average<=80:
    print("medical")
else:
    ("fail")

