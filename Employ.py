class Employee:

    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary = salary

    def get_details(self):
        print(f"The Employee with {self.name} and {self.email} has salary {self.salary :.2f}")


class Manager(Employee):
    def promote(self, employee : Employee):
        employee.salary *= 1.10 
        
        # return employee.salary


class Developer(Employee):
    def __init__(self, name, email, salary, programming_language):
        super().__init__(name, email, salary)
        self.programming_language = programming_language

    def get_details(self):
        print(f"The Employee with {self.name} and {self.email} has salary {self.salary :.2f} and knows Programming language: {self.programming_language}")

manager = Manager('George P', 'george@gmail.com', 2000)
developer = Developer('Lampros P','lampros@gmail.com', 1000, "Backend developer")

manager.get_details()
developer.get_details()

manager.promote(developer)
developer.get_details()