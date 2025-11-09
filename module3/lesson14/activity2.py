
class Vehicle:
    #create init method
    def __init__(self,max_speed,mileage):
        #bind the arguement
        self.max_speed=max_speed
        self.mileage=mileage
#  object variation
modelX=Vehicle(max_speed=40,mileage=80)
#access the variables inside init method
print("Model Max Speed",modelX.max_speed)
print("Model Mileage:",modelX.mileage)



