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

class Client:
  def __init__(self, clientID, name, address, contactDetails, budget):
    self.clientID = clientID
    self.name = name
    self.address = address
    self.contactDetails = contactDetails
    self.budget = budget

class Guest: 
  def __init__(self, guestID, name, address, contactDetails):
    self.guestID = guestID
    self.name = name 
    self.address = address
    self.contactDetails = contactDetails

class Event: 
  def __init(self, eventID, eventType, theme, date, time, duration, venueAddress, client, guests):
    self.eventID = eventID
    self.eventType = eventType
    self.theme = theme
    self.date = date
    self.time = time
    self.duration = duration
    self.venueAddress = venueAddress
    self.client = client
    self.guests = guests
    self.suppliers = []

class Supplier:
  def __init__(self, supplierID, name, address, contactDetails):
    self.supplierID = supplierID
    self.name = name
    self.address = address
    self.contactDetails = contactDetails

class CateringCompany(Supplier):
  def __init__(self, supplierID, name, address, contactDetails, menu):
    super().__init__(supplierID, name, address, contactDetails)
    self.menu = menu

class CleaningCompany(supplier):
  pass

class DecorationsCompany(supplier):
  pass

class EntertainmentCompany(supplier):
  pass

class FurnitureSupplyCompany(supplier):
  pass

class Venue:
  def __init__(self, venueID, name, address, contact, minGuests, maxGuests):
    self.venueID = venueID
    self.name = name
    self.address = address
    self.contact = contact
    self.minGuests = minGuests
    self.maxGuests = maxGuests
  


























