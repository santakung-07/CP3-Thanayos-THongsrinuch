# lecture 105 inheritance of Parent class to child class
class Vehicle:
    licenseCode = ""
    serialCode = ""

    def turnOnAirCondition(self):
        print("Turn On: Air")
class Car(Vehicle):     
    pass
class PickUp(Vehicle):      
    pass
class Van(Vehicle):
    pass
class EstateCar(Vehicle):
    pass
car1 = Car()       
car1.turnOnAirCondition()
pickUp1 = PickUp()       
pickUp1.turnOnAirCondition()
van1 = Van()       
van1.turnOnAirCondition()
estateCar1 = EstateCar()       
estateCar1.turnOnAirCondition()