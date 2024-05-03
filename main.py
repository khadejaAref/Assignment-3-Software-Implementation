from datetime import date, time

class Employee:
  def __init__(self, name, idNumber, department, jodTitle, basicSalary, age, dateOfBirth, passportDetails):
    self.name = name
    self.idNumber = idNumber
    self.department = department
    self.jodTitle = jodTitle
    self.basicSalary = basicSalary
    self.age = age
    self.dateOfBirth = dateOfBirth
    self.passportDetails = passportDetails

class SalesManager(Employee):
  def __init__(self, name, idNumber, department, jodTitle, basicSalary, age, dateOfBirth, passportDetails):
    super().__init__(self, name, idNumber, department, jodTitle, basicSalary, age, dateOfBirth, passportDetails)
    self.manages = []

class Salesperson(Employee):
  def __init__(self, name, idNumber, department, jodTitle, basicSalary, age, dateOfBirth, passportDetails, salary, manager):
    super().__init__(self, name, idNumber, department, jodTitle, basicSalary, age, dateOfBirth, passportDetails)
    self.salary = salary
    self.manager = manager

class MarketingManager(Employee):
  pass

class Marketer(Employee):
  pass

class Accountant(Employee):
  pass

class Designer(Employee):
  pass

class Handyman(Employee):
  pass









