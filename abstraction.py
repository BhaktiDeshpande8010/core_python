from abc import ABC,abstractclassmethod

class Payment(ABC):
    def print_slip(self,amount):
        print("Your payment was done with Rs.",amount)

        @abstractclassmethod
        def payment(self):
            print("a")      #this section will not get print this is the abstract code the hidded  one

class credit(Payment):
    def payment(self,amount):
        print("Credit crd payment done with Rs.",amount)

c=credit()
c.payment(1000)
c.print_slip(5000)