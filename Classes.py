class Trainer:

    def __init__(self):
        self.name = None
        self.__salary = 1000  # double underscore before slary ensures that this variable is not accessible outside this class

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def __str__(
            self):  # It is a inbuilt function which by defaults on printing just object gives its address, here we have redifined the function
        return self.name + " " + str(self.__salary)


lion_trainer = Trainer()
lion_trainer.name = "john"

print(lion_trainer.name)
print(lion_trainer._Trainer__salary)

monkey_trainer = Trainer()
monkey_trainer.name = "Leo"

print(monkey_trainer.name)

lion_trainer.set_salary(4000)
print(lion_trainer.get_salary())

lion = Trainer()
lion.name = "Pranav"
lion.salary = 2000
print(lion.salary)
print(lion_trainer)


class elephant:
    def __init__(self):
        self.__age = None
        self.__tusk_length = None

    def set_tusk(self, tusk):
        self.__tusk_length = tusk

    def get_tusk(self):
        return self.__tusk_length

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def dance(self):
        if self.__age < 5:
            print("Dance for 1 minute")
        else:
            print("dance till eternity")


myElephant = elephant()
myElephant.set_age(2)
print(myElephant.get_age())
myElephant.set_tusk(23)
print(myElephant.get_tusk())
myElephant.dance()
