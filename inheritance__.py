class circusAnimals:
    def eat(self,food):
        print("Eat daily",food)

    def sleep(self,hours):
        print("sleep for: ",hours," hours")

class Monkey(circusAnimals):
    def ride_cycle(self):
        print("Ride Cycle")

class Elephant(circusAnimals):
    def dance(self):
        print("Dance")
    def eat(self,food,med):
        print("have food: ",food)
        print("Have medicine: ",med)


m=Monkey()
m.eat("banana")
m.sleep(8)
m.ride_cycle()

e=Elephant()
e.eat("Sugar","crocin")
e.sleep(8)
e.dance()