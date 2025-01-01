#open("work2.txt,"x")
#f=open("work2.txt,"w")
#f.write("kaviya")
#f=open("work2.txt","a")
#f.write("\nname\tag")
#f=open("work2.txt","r")
#a=f.read()
#print(a)
class student:
    def __init__(self,name,age,qualify,address):
       self.name=name
       self.age=age
       self.qualify=qualify
       self.address=address
    def printdetail(self):
        print(self.name,self.age,self.qualify,self.address)
class inform(student):
    pass
x=inform("S.kaviya",19,"qualify BSC","address thirukkadaiyur")
x.printdetail()


