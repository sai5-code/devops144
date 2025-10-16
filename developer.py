from employee import Employee
class Developer:
    def __init__(self,name,dept,salary,programming_lang):
        Employee.__init__(self,name,dept,salary)
        self.programming_lang=programming_lang
    def __repr__(self):
        return f"Developer(Name: {self.name}, Dept: {self.dept}, Salary: {self.salary}, Programming Language: {self.programming_lang})"
    def add_employee(self):
        Employee.add_employee(self)
    def remove_employee(self,name):
        Employee.remove_employee(self,name)

    