from database import Employee

class Manager(Employee):
    def __init__(self, firstName, lastName, age, department, salary, managed_department):
        super().__init__(firstName, lastName, age, department, salary)
        self.managed_department = managed_department

    def show(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print("Salary: Confidential")  
        print(f"Managed Department: {self.managed_department}")


def menu():
    while True:
        print("Menu:")
        print("1. Add new employee")
        print("2. Add new manager")
        print("3. Exit")
        choice = input("Enter the number corresponding to your choice: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            add_manager()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid number.")


def add_employee():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = input("Enter age: ")
    department = input("Enter department: ")
    salary = input("Enter salary: ")
    employee = Employee(first_name, last_name, age, department, salary)
    print("Employee added successfully.\n")


def add_manager():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = input("Enter age: ")
    department = input("Enter department: ")
    salary = input("Enter salary: ")
    managed_department = input("Enter managed department: ")
    manager = Manager(first_name, last_name, age, department, salary, managed_department)
    print("Manager added successfully.\n")


# Main function
if __name__ == "__main__":
    menu()
