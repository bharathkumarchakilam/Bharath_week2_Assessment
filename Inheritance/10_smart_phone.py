#base class Electronics
class Electronics:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"\nBrand: {self.brand}, Model: {self.model}")

#class MobileDevice inheriting from Electronics
class MobileDevice(Electronics):
    def __init__(self, brand, model, os):
        super().__init__(brand, model)  
        self.os = os

    def display_info(self):
        super().display_info()
        print(f"Operating System: {self.os}")

#derived class SmartPhone inheriting from MobileDevice
class SmartPhone(MobileDevice):
    def __init__(self, brand, model, os, camera_megapixels):
        super().__init__(brand, model, os)
        self.camera_megapixels = camera_megapixels

    def display_info(self):
        super().display_info()  
        print(f"Camera: {self.camera_megapixels} MP")

brand = input("Enter the brand of the smartphone: ")
model = input(f"Enter the model of the {brand}: ")
os = input(f"Enter the operating system of the {brand}: ")
camera_megapixels = int(input(f"Enter the camera megapixels of the {brand}: "))

#create a SmartPhone object
smartphone = SmartPhone(brand,model,os,camera_megapixels)

#call the display_info method to show smartphone details
smartphone.display_info()
