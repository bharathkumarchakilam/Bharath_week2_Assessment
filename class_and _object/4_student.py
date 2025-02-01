#class for adding and displaying the student details
class Student:
    students = []

    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        Student.students.append(self)
    
    #function for displaying the student details
    def get_details(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}"
    
    #function for displaying the all student details
    def display_all_students():
        if not Student.students:
            print("No students available.")
        else:
            for student in Student.students:
                print(student.get_details())


def main():
    while True:
        name = input("Enter student name (or type 'exit' to stop): ")
        if name == "exit":
            break
        roll_number = input("Enter roll number: ")
        Student(name, roll_number)

    # Displaying all students simultaneously
    print("\nList of Students:")
    Student.display_all_students()

main()