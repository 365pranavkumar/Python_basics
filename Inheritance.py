class circusAnimals:
    def bow_before_performance(self):
        print("Bowing before")

    def wave_after_performance(self,counter):
        wave_counter=0;
        while(wave_counter<counter):
            print("Wave")
            wave_counter+=1

class Monkey(circusAnimals):
    def ride_cycle(self):
        self.bow_before_performance()
        print("Ride cycle")
        self.wave_after_performance(3)

class Elephant(circusAnimals):
    def dance(self):
        self.bow_before_performance()
        print("Dance ")
        self.wave_after_performance(3)

class Lion(circusAnimals):
    def dance_on_cycle(self):
        self.bow_before_performance()
        print("Dance on cycle")
        self.wave_after_performance(3)

doodoo = Monkey()
doodoo.ride_cycle()

looloo = Elephant()
looloo.dance()

booboo = Lion()
booboo.dance_on_cycle()