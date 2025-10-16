from employee import Employee
class HR:

    def __init__(self,name,dept,salary,domain):
        Employee.__init__(self,name,dept,salary) 
        self.domain=domain
        
    def __repr__(self):
        return f"Employee: (name:{self.name},dept:{self.dept},salary:{self.salary},domain:{self.domain})"
    
    def add_employee(self):
        Employee.add_employee(self)
    def remove_employee(self,name):
        Employee.remove_employee(self,name)
        