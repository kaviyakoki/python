class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printname(self):
        print(self.name,self.age)
class school(person):
    def __init__(self,name,age,school):
        super(). __init__(name,age)
        self.school=school
    def print(self):
        print(self.name,self.age,self.school)
class student(school):
    def __init__(self,name,age,school,group):
        super(). __init__(name,age,school)
        self.group=group
nivee=student("nivee","yass","annai","b.tech")
nivee.printname()
nivee.print()
print(nivee.group)
        

