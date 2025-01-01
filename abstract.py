from abc import ABC,abstractmethod
class bank(ABC):
    def bank_info(self):
        print("welcome to bank")
    def interest(self):
        pass

#subclass /child class of abstract class
class SBI(bank):
    def interest(self):
        print("hi")
    def balance(self):
        print("balance in 100")
s=SBI()
s.bank_info()
s.balance()
s.interest()