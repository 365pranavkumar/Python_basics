class vehicle:
    def __init__(self):
        self.__mileage = None
        self.__fuel_left = None
        self.__initial_fuel = None

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def get_mileage(self):
        return self.__mileage

    def set_fleft(self, fleft):
        self.__fuel_left = fleft

    def get_fleft(self):
        return self.__fuel_left

    def set_ifuel(self, ifuel):
        self.__initial_fuel = ifuel

    def get_ifuel(self):
        return self.__initial_fuel

    def dis_travel(self):
        d = self.__initial_fuel - self.__fuel_left
        e = d * self.__mileage
        return e

    def dis_left(self):
        self.__fuel_left = self.__fuel_left - 5
        dis = self.__mileage * self.__fuel_left
        return dis


car = vehicle()
car.set_mileage(10)
car.set_fleft(35)
car.set_ifuel(60)
print("Total distance travel till now is: ", car.dis_travel(), "kms")
print("Total distance that can be travelled is: ", car.dis_left(), "kms")
