class Employee:
    total_employees=[]
    def __init__(self,name,dept,salary):
        self.name = name
        self.dept = dept
        self.salary = salary
    
    def __repr__(self):
        return f"Employee(Name: {self.name}, Dept: {self.dept}, Salary: {self.salary})"
    
    def add_employee(self):
        Employee.total_employees.append(self)
        return f"Employee {self.name} added successfully."
    
    def remove_employee(self, name):
        for emp in Employee.total_employees:
            if emp.name == name:
                Employee.total_employees.remove(emp)
                return f"Employee {name} removed successfully."
        return f"Employee {name} not found."