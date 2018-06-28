class Monkey:
    __no_of_bananas = 40

    def eat_banana(self):
        print("Eat banana")
        Monkey.__no_of_bananas = Monkey.__no_of_bananas - 1

    @staticmethod
    def get_banana_count():  # When using static method self is not used but the class name is
        print("Bananas left: ", Monkey.__no_of_bananas)


m1 = Monkey()
m2 = Monkey()

m1.eat_banana()
Monkey.get_banana_count()
m2.eat_banana()
Monkey.get_banana_count()
m1.eat_banana()
Monkey.get_banana_count()


class Demo:
    num = 5

    def __init__(self, status):
        #num = 10
        print(status)
        print(num).0


print(Demo('A'))
print(Demo.num)
