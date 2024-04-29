import pymongo

class Employee:
    employees = []

    # Constructor
    def __init__(self, firstName, lastName, age, department, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.department = department
        self.salary = salary

        Employee.employees.append(self)

        # insert document
        self.insert()

    # Connect to database function
    def connectDatabase(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["employee_database"]
        collection = db["employees"]
        return collection, client

    # Insert document function
    def insert(self):
        # connect to database
        collection, client = self.connectDatabase()

        employee = {
            "fName": self.firstName,
            "lName": self.lastName,
            "age": self.age,
            "department": self.department,
            "salary": self.salary
        }

        collection.insert_one(employee)

        client.close()

    # Transfer department function
    def transfer(self, new_department):
        self.department = new_department

        # connect to database
        collection, client = self.connectDatabase()

        employee = {"fName": self.firstName, "lName": self.lastName}
        updateDepartment = {"$set": {"department": new_department}}
        collection.update_one(employee, updateDepartment)
        client.close()

    # Remove the employee
    def fire(self):
        Employee.employees.remove(self)

        # connect to database
        collection, client = self.connectDatabase()

        employee = {"fName": self.firstName, "lName": self.lastName}
        collection.delete_one(employee)
        client.close()

    # Display the employee
    def show(self):
        print(f"First Name: {self.firstName}")
        print(f"Last Name: {self.lastName}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")

    @staticmethod
    def list_employees():
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["employee_database"]
        collection = db["employees"]
        for employee_data in collection.find():
            print(employee_data)
        client.close()


employee1 = Employee("mohamed", "torkey", 22, "ITI", 4000)

employee1.transfer("HR")

employee1.show()

Employee.list_employees()

