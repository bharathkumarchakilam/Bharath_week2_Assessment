#base class Animal
class Animal:
    def speak(self):
        pass
    
#derived class Cat inheriting from Animal   
class Dog(Animal):
    def speak(self):
        return "Dog says Woof!"


#derived class Cat inheriting from Animal
class Cat(Animal):
    def speak(self):
        return "cat says Meow!"
    
#creating Dog and Cat objects
dog = Dog()
cat = Cat()

# Calling speak method for Dog and Cat objects
print(dog.speak()) 
print(cat.speak())  
