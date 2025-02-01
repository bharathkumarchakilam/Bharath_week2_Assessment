#importing the abstractmethod from abc module
from abc import ABC, abstractmethod

class IVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass

class Car(IVehicle):
    def start_engine(self):
        print("Car engine started")
    
    def stop_engine(self):
        print("Car engine stopped")

class Bike(IVehicle):
    def start_engine(self):
        print("Bike engine started")
    
    def stop_engine(self):
        print("Bike engine stopped")

class Truck(IVehicle):
    def start_engine(self):
        print("Truck engine started")
    
    def stop_engine(self):
        print("Truck engine stopped")

vehicle_type = input("Enter vehicle type (Car, Bike, Truck): ")

if vehicle_type == "Car":
    vehicle = Car()
elif vehicle_type == "Bike":
    vehicle = Bike()
elif vehicle_type == "Truck":
    vehicle = Truck()
else:
    print("Invalid vehicle type")
    exit()

vehicle.start_engine()
vehicle.stop_engine()
