#base class Person
class Person:
    def __init__(self, name, age):
        self.name = name  #person's name
        self.age = age    #person's age

    def display_info(self):
        """Displays personal details."""
        print(f"Name: {self.name}, Age: {self.age}")


#derived class Employee inheriting from Person
class Employee(Person):
    def __init__(self, name, age, emp_id, department):
        super().__init__(name, age)  
        self.emp_id = emp_id         
        self.department = department 
        
    #displays employee details.
    def display_info(self):
        super().display_info() 
        print(f"Employee ID: {self.emp_id}, Department: {self.department}")


#multi-level inheritance: Manager inheriting from Employee
class Manager(Employee):
    def __init__(self, name, age, emp_id, department, team_size):
        super().__init__(name, age, emp_id, department) 
        self.team_size = team_size  
        
    #displays manager details.
    def display_info(self):
        super().display_info()  
        print(f"Team Size: {self.team_size}")
        
    #approves leave for an employee.
    def approve_leave(self, employee_name, days):
        print(f"Manager {self.name} has approved {days} days leave for {employee_name}.")

#creating a Person object
print("Person Details:")
person = Person("Alice", 30)
person.display_info()

#creating an Employee object
print("\nEmployee Details:")
employee = Employee("Bob", 25, "E101", "IT")
employee.display_info()

#creating a Manager object
print("\nManager Details:")
manager = Manager("Charlie", 40, "M201", "HR", 10)
manager.display_info()

#approving leave using Manager
print("\nLeave Approval:")
manager.approve_leave("Bob", 5)
