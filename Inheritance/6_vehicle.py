#base class Vehicle
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand  # Vehicle brand
        self.model = model  # Vehicle model
        
    #function  displays the brand and model of the vehicle
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")


#derived class Car inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  
        self.doors = doors
    
    #function displays brand and model from Vehicle class
    def display_info(self):
        super().display_info()  
        print(f"Number of doors: {self.doors}")


#derived class Bike inheriting from Vehicle
class Bike(Vehicle):
    def __init__(self, brand, model, type_bike):
        super().__init__(brand, model)  
        self.type_bike = type_bike 
        
    #function displays brand and model from Vehicle class
    def display_info(self):
        super().display_info()
        print(f"Bike Type: {self.type_bike}")
        
#derived class ElectricCar inheriting from Car
class ElectricCar(Car):
    def __init__(self, brand, model, doors, battery_capacity):
        super().__init__(brand, model, doors)  
        self.battery_capacity = battery_capacity  
        
    #function displays brand, model, and doors from Car class
    def display_info(self):
        super().display_info() 
        print(f"Battery Capacity: {self.battery_capacity} kWh")

#creating an object of Car
print("Car Details:")
car = Car("Toyota", "Corolla", 4)

#display details of the car
car.display_info()  

#creating an object of Bike
print("\nBike Details:")
bike = Bike("Yamaha", "MT-15", "Sports")

#display details of the bike
bike.display_info() 

#creating an object of ElectricCar
print("\nElectric Car Details:")
e_car = ElectricCar("Tesla", "Model 3", 4, 75)

#display details of the electric car
e_car.display_info() 
