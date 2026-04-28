from abc import ABC,abstractclassmethod

class Payment(ABC):
    def print_slip(self,amount):
        print("Your payment was done with Rs.",amount)

        @abstractclassmethod
        def payment(self):
            print("a")    

class credit(Payment):
    def payment(self,amount):
        print("Credit crd payment done with Rs.",amount)

c=credit()
c.payment(1000)
c.print_slip(5000)