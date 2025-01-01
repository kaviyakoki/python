class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def var(self):
        print(f"i am cat,my name is{self.name}.i am{self.age}years old.")
    def sound(self):
        print("meow")
class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def var(self):
        print(f"i am dog,my name is {self.name}.i am{self.age}years old.")
    def sound(self):
        print("bark")
class lion:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def var(self):
        print(f"i am lion,my name is{self.name}.i am{self.age}years old")
    def sound(self):
        print("roar")
cat1=cat("kitty",4)
dog1=dog("puppy",5)
lion1=lion("cub",6)
for animal in(cat1,dog1,lion1):
    animal.sound()
    animal.var()    