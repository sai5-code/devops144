from employee import Employee
from hr import HR
from tester import Tester
from developer import Developer

e1=Employee("sai","it",20000)
e2=HR("ram","it",30000,"management")
e3=Tester("hari","web",20000,"python")
e4=Developer("bob","it",30000,"java")

e1.add_employee()
e2.add_employee()
e3.add_employee()
e4.add_employee()

print(Employee.total_employees)

e1.remove_employee("sai")

print(Employee.total_employees)
e1=Employee("sai","it",20000)
print(Employee.total_employees)
