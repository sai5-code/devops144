from employee import Employee
class Tester:
    def __init__(self,name,dept,salary,tool):
        Employee.__init__(self,name,dept,salary) 
        self.debugging_tool=tool
        
    def __repr__(self):
        return f"Employee: (name:{self.name},dept:{self.dept},salary:{self.salary},debugging_tool:{self.debugging_tool})"
    
    def add_employee(self):
        Employee.add_employee(self)
    def remove_employee(self,name):
        Employee.remove_employee(self,name)
    
    
    