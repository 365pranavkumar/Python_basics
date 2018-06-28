class shelter:
    def __init__(self,shelter_for):
        self.shelter_for=shelter_for

class tent(shelter):
    def __init__(self,shelter_for,no_of_cots,no_of_chairs):
        super(shelter_for)
        self.no_of_cots=no_of_cots
        self.no_of_chairs=no_of_chairs

class cage(shelter):
    def __init__(self,shelter_for,type_of_lock):
        self.type_of_lock=type_of_lock
