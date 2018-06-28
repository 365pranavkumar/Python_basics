class monkey:
    def __init__(self):
        self.breed = None
        self.color = None

    def ride_cycle(self):
        if self.breed == "chimpanzee":
            print("\nRide cycle for one minute")
        else:
            print("\nRide cycle till eternity")


a = monkey()
a.breed = "gorilla"
a.color = "black"

b = monkey()
b.breed = "chimpanzee"
b.color = "Rainbow"

c = monkey()
c.breed = "gorilla"
c.color = "rang biranga"

d = monkey()
d.breed = "chimpanzee"
d.color = "Nothing special, as usual black"

print("Monkey 1 color is: ", a.color)
print("Monkey 1 breed is: ", a.breed)

print("\nMonkey 2 color is: ", b.color)
print("Monkey 2 breed is: ", b.breed)

print("\nMonkey 3 color is: ", c.color)
print("Monkey 3 breed is: ", c.breed)

print("\nMonkey 4 color is: ", d.color)
print("Monkey 4 breed is: ", d.breed)

list = {a, b, c, d}
for monkey in list:
    monkey.ride_cycle()



