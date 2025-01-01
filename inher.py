'''
class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def name(self):
        print(self.firstname,self.lastname)
class student(person):
    pass
x=student("sk","kaviya")
x.name()

class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def name(self):
        print(self.firstname , self.lastname)
class student(person):
    def __init__(self,fname,lname):
        super(). __init__(fname,lname)
        person. __init__(self,fname,lname)
        self.graduationyear=2024
x=student("kaviya","bdkn")
print(x.graduationyear)
x.name()

class detail:
    def __init__(self,age,birth):
        self.age=age
        self.birth=birth
    def mine(self):
        print(self.age,self.birth)
class personal(detail):
    pass
x=personal(18,2005)
x.mine()

'''