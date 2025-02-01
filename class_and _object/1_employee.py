#class for adding and dispalying the employee details
class Employee:
    employees = []
    #consturctor for getting the employee details
    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        Employee.employees.append(self)
        
    #function for display the employee details
    def get_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Department: {self.department}\n")
        
    #function for displaying the all employees details
    def display_all():
        if not Employee.employees:
            print("No employees available.")
        else:
            print("\nEmployee Details:")
            for emp in Employee.employees:
                emp.get_details()

#main function
def main(): 
    while True:
        name = input("Enter employee name or (enter 's' to stop): ")
        if name == "s" or name == 'S':
            break
        emp_id = input("Enter employee ID: ")
        department = input("Enter employee department: ")
        
        Employee(name, emp_id, department)

    # Displaying all employee details
    Employee.display_all()

#run the program    
main()
