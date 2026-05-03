# encapsulation 
# access modifier :public

class python:
    id=0;
    name=""

    def __init__(self,id,name):
        self.id=id
        self.name=name

        # print(self.id)
        # print(self.name)

p=python(101,"program")
print(p.id)
print(p.name)


# private access modifier
class temp:      
    __id=0;                               #use to __(sunder )
    __name=""

    def __init__(self,__id,__name):
        self.__id=__id
        self.__name=__name

        print(self.__id)
        print(self.__name)

t=temp(101,"program")


class fortune:
    _cyber="security"
    _wifi="5g"

class cravita(fortune):
    # def __init__(self):
    #     print(self._wifi)
    #     print(self._cyber)

    def profile(self):
        print(self._wifi)
        print(self._cyber)

c=cravita()
