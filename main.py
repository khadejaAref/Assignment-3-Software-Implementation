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
    
  def get_name(self):
    return self._name

  def set_name(self, name):
    self._name = name

  def get_idNumber(self):
    return self._idNumber

  def set_idNumber(self, idNumber):
    self._idNumber = idNumber

  def get_department(self):
    return self._department

  def set_department(self, department):
    self._department = department

  def get_jobTitle(self):
    return self._jobTitle

  def set_jobTitle(self, jobTitle):
    self._jobTitle = jobTitle

  def get_basicSalary(self):
    return self._basicSalary

  def set_basicSalary(self, basicSalary):
    self._basicSalary = basicSalary

  def get_age(self):
    return self._age

  def set_age(self, age):
    self._age = age

  def get_dateOfBirth(self):
    return self._dateOfBirth

  def set_dateOfBirth(self, dateOfBirth):
    self._dateOfBirth = dateOfBirth

  def get_passportDetails(self):
    return self._passportDetails

  def set_passportDetails(self, passportDetails):
    self._passportDetails = passportDetails


class SalesManager(Employee):
  def __init__(self, name, idNumber, department, jodTitle, basicSalary, age, dateOfBirth, passportDetails):
    super().__init__(self, name, idNumber, department, jodTitle, basicSalary, age, dateOfBirth, passportDetails)
    self.manages = []

  def get_manages(self):
    return self._manages

  def set_manages(self, manages):
    self._manages = manages

class Salesperson(Employee):
  def __init__(self, name, idNumber, department, jodTitle, basicSalary, age, dateOfBirth, passportDetails, salary, manager):
    super().__init__(self, name, idNumber, department, jodTitle, basicSalary, age, dateOfBirth, passportDetails)
    self.salary = salary
    self.manager = manager

  def get_salary(self):
    return self._salary

  def set_salary(self, salary):
    self._salary = salary

  def get_manager(self):
    return self._manager

  def set_manager(self, manager):
    self._manager = manager

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

  def get_clientID(self):
    return self._clientID

  def set_clientID(self, clientID):
    self._clientID = clientID

  def get_name(self):
    return self._name

  def set_name(self, name):
    self._name = name

  def get_address(self):
    return self._address

  def set_address(self, address):
    self._address = address

  def get_contactDetails(self):
    return self._contactDetails

  def set_contactDetails(self, contactDetails):
    self._contactDetails = contactDetails

  def get_budget(self):
    return self._budget

  def set_budget(self, budget):
    self._budget = budget

class Guest: 
  def __init__(self, guestID, name, address, contactDetails):
    self.guestID = guestID
    self.name = name 
    self.address = address
    self.contactDetails = contactDetails

  def get_guestID(self):
    return self._guestID

  def set_guestID(self, guestID):
    self._guestID = guestID

  def get_name(self):
    return self._name

  def set_name(self, name):
    self._name = name

  def get_address(self):
    return self._address

  def set_address(self, address):
    self._address = address

  def get_contactDetails(self):
    return self._contactDetails

  def set_contactDetails(self, contactDetails):
    self._contactDetails = contactDetails

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

  def get_eventID(self):
    return self._eventID

  def set_eventID(self, eventID):
    self._eventID = eventID

  def get_eventType(self):
    return self._eventType

  def set_eventType(self, eventType):
    self._eventType = eventType

  def get_theme(self):
    return self._theme

  def set_theme(self, theme):
    self._theme = theme

  def get_date(self):
    return self._date

  def set_date(self, date):
    self._date = date

  def get_time(self):
    return self._time

  def set_time(self, time):
    self._time = time

  def get_duration(self):
    return self._duration

  def set_duration(self, duration):
    self._duration = duration

  def get_venueAddress(self):
    return self._venueAddress

  def set_venueAddress(self, venueAddress):
    self._venueAddress = venueAddress

  def get_client(self):
    return self._client

  def set_client(self, client):
    self._client = client

  def get_guests(self):
    return self._guests

  def set_guests(self, guests):
    self._guests = guests

  def get_suppliers(self):
    return self._suppliers

  def set_suppliers(self, suppliers):
    self._suppliers = suppliers


class Supplier:
  def __init__(self, supplierID, name, address, contactDetails):
    self.supplierID = supplierID
    self.name = name
    self.address = address
    self.contactDetails = contactDetails

  def get_supplierID(self):
    return self._supplierID

  def set_supplierID(self, supplierID):
    self._supplierID = supplierID

  def get_name(self):
    return self._name

  def set_name(self, name):
    self._name = name

  def get_address(self):
    return self._address

  def set_address(self, address):
    self._address = address

  def get_contactDetails(self):
    return self._contactDetails

  def set_contactDetails(self, contactDetails):
    self._contactDetails = contactDetails

class CateringCompany(Supplier):
  def __init__(self, supplierID, name, address, contactDetails, menu):
    super().__init__(supplierID, name, address, contactDetails)
    self.menu = menu

  def get_menu(self):
    return self._menu
    
  def set_menu(self, menu):
    self._menu = menu

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

  def get_venueID(self):
    return self._venueID

  def set_venueID(self, venueID):
    self._venueID = venueID

  def get_name(self):
    return self._name

  def set_name(self, name):
    self._name = name

  def get_address(self):
    return self._address

  def set_address(self, address):
    self._address = address

  def get_contact(self):
    return self._contact

  def set_contact(self, contact):
    self._contact = contact

  def get_minGuests(self):
    return self._minGuests

  def set_minGuests(self, minGuests):
    self._minGuests = minGuests

  def get_maxGuests(self):
    return self._maxGuests

  def set_maxGuests(self, maxGuests):
    self._maxGuests = maxGuests
  


























