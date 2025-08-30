class Employee:
    def __init__(self, emp_id, ename, salary):
      self.ep_id = emp_id
      self.ename = ename
      self.salary = salary
    def showname(self):
      print("Employee ID:", self.ep_id)
    def showsalary(self):
      print("Employee Name:", self.ename)
      print("Employee Salary:", self.salary)
e1  = Employee(101,"lullu" ,100000)
e1.showname()
e1.showsalary()