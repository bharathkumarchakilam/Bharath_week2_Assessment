#base class Car
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Car brand
        self.model = model  # Car model

    # function for moving the car on the road
    def move(self):
        print(f"The {self.brand} {self.model} is driving on the road.")


#base class Airplane
class Airplane:
    def __init__(self, brand, model):
        self.brand = brand  
        self.model = model 

    # function for flying the airplane in the sky
    def move(self):
        print(f"The {self.brand} {self.model} is flying in the sky.")


#derived class FlyingCar inheriting from both Car and Airplane
class FlyingCar(Car, Airplane):
    def __init__(self, brand, model):
        Car.__init__(self, brand, model)    
        Airplane.__init__(self, brand, model)  

    # function for handling movement, considering both Car and Airplane behavior
    def move(self):
        print(f"The {self.brand} {self.model} is moving in the sky and on the road.")
        Car.move(self) 
        Airplane.move(self)
        
        
#create an object of FlyingCar
flying_car = FlyingCar("Tesla", "Model X")

#call the move function for FlyingCar
flying_car.move()
