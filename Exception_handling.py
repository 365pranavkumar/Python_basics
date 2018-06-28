class lessFoodException(Exception):
    def __init__(self,food_quantity):
        message = "Food given was"+str(food_quantity)+"kg. Please increase food quantity"
        super().__init__(message)

class moreFoodException(Exception):
    def __init__(self,food_quantity):
        message = "Food given was"+str(food_quantity)+"kg. Please decrease food quantity"
        super().__init__(message)




class Staff:
    def feed_animal(self,animal,food_quantity):
        if food_quantity<5:
            raise lessFoodException(food_quantity)

        elif food_quantity>15:
            #raise Exception
            raise moreFoodException(food_quantity)
        else:
            raise Exception

class Monkey:
    pass
class FoodAnchor:
    def send_food(self,animal,staff,food_quality):
        staff.feed_animal(animal,food_quality)

    def gossip(self):
        print("Waste time in gossip")

food_anchor = FoodAnchor()
chimpu = Monkey()
circus_staff = Staff()
try:
    food_anchor.send_food(chimpu,circus_staff,2)
    food_anchor.gossip()

except lessFoodException as e:
    print(e)

except moreFoodException as e:
    print(e)

#except Exception:
 #   print("food is not proper")


finally:
    print("Thank you")






