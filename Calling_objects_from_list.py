from abc import ABCMeta,abstractmethod
class circusAnimals(metaclass=ABCMeta):
    def eat(self,food):
        print("eat meal: ",food)
    @abstractmethod
    def perform_trick(self):
        pass
    def sleep(self,hours):
        print("sleep for: ",hours)

class Monkey(circusAnimals):
    def perform_trick(self):
        print("[FOR MONKEY]\nRide the cycle\n")

class Elephant(circusAnimals):
    def perform_trick(self):
        print("[FOR ELEPHANT]\ndance\n")

class Lion(circusAnimals):
    def perform_trick(self):
        print("[FOR LION]\nJump\n")

#class Hippo(circusAnimals):  #Since perform_trick is an abstract class.therefore must be present in all inherited classes,otherwise we will get an error in output
 #   def stand(self):
  #      print("stand")

m=Monkey()
e=Elephant()
l=Lion()
#h=Hippo()

list_of_animals=[m,e,m,l,l,e]
for animal in list_of_animals:
    animal.perform_trick()