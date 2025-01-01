'''
class c1:
    def __init__(self,year,course):
        self.year=year
        self.course=course
        print("this is a function")
    def func1(self):
        print(self.year,self.course)
c=c1("second","python")
c.func1()
''' 
class employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        print("salary is increase in monthly")
    def read(self):
        print(self.name,self.age,self.salary)
    def __str__(self):
        return str(self.age)
obj=employee("indhu",23,15000)
obj.read()
print(obj)


