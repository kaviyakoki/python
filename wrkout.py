name=[]
age=[]
fathername=[]
mothername=[]
place=[]
address=[]
for x in range(3):
    name.append(input("enter a name:"))
    age.append(int(input("enter a age:")))
    fathername.append(input("enter a fathername:"))
    mothername.append(input("enter a mothername:"))
    place.append(input("enter a place:"))
    address.append(input("enter a address:"))
if age>18:
    place="mayiladuthurai"
    print("eligible")
else:
    print("not")




