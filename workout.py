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
x=inform("kaviya",19,"BSC","thirukkadaiyur")
x.printdetail()


