from tkinter import *
from tkinter import messagebox
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

class CleaningCompany(Supplier):
  pass

class DecorationsCompany(Supplier):
  pass

class EntertainmentCompany(Supplier):
  pass

class FurnitureSupplyCompany(Supplier):
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

class EventManagementApp:
  def __init__(self, master):
    self.master = master
    master.title("Event Management System")
    
    self.label = Label(master, text="Welcome to Event Management System")
    self.label.pack()
    
    # Buttons to open different windows for different functionalities
    self.employee_button = Button(master, text="Employees", command=self.open_employee_window)
    self.employee_button.pack()

    self.event_button = Button(master, text="Events", command=self.open_event_window)
    self.event_button.pack()

    self.client_button = Button(master, text="Clients", command=self.open_client_window)
    self.client_button.pack()

    self.guest_button = Button(master, text="Guests", command=self.open_guest_window)
    self.guest_button.pack()

    self.supplier_button = Button(master, text="Suppliers", command=self.open_supplier_window)
    self.supplier_button.pack()

    self.venue_button = Button(master, text="Venues", command=self.open_venue_window)
    self.venue_button.pack()
    
  # Functions to open different windows for each functionality
  # Add/Delete/Modify/Display employee details
  def open_employee_window(self):
    employee_window = Toplevel(self.master)
    employee_window.title("Employee Management")
 
# Add/Delete/Modify/Display event details 
  def open_event_window(self):
    event_window = Toplevel(self.master)
    event_window.title("Event Management")

# Add/Delete/Modify/Display client details 
  def open_client_window(self):
    client_window = Toplevel(self.master)
    client_window.title("Client Management")

# Add/Delete/Modify/Display guest details 
  def open_guest_window(self):
    guest_window = Toplevel(self.master)
    guest_window.title("Guest Management")

# Add/Delete/Modify/Display supplier details 
  def open_supplier_window(self):
    supplier_window = Toplevel(self.master)
    supplier_window.title("Supplier Management")

# Add/Delete/Modify/Display venue details 
  def open_venue_window(self):
    venue_window = Toplevel(self.master)
    venue_window.title("Venue Management")
  

#test cases
if __name__ == '__main__':
  root = Tk()
  app = EventManagementApp(root)
  root.mainloop()
  #create employees
  sales_manager1 = SalesManager("Susan Meyers", 47899, "Sales", "Manager", 37500, 35, date(1989, 5, 15), "AB123456")
  sales_manager2 = SalesManager("Joy Rogers", 81774, "Sales", "Manager", 24000, 32, date(1992, 3, 6), "ABC67890")
  salesperson1 = Salesperson("Shyam Sundar", 11234, "Sales", "Salesperson", 20000, 28, date(1996, 9, 10), "CD987654", 15000, sales_manager1)
  salesperson2 = Salesperson("Salma J Sam", 98637, "Sales", "Salesperson", 20000, 30, date(1994, 2, 25), "EF654321", 15000, sales_manager1)
  salesperson3 = Salesperson("Mariam Khalid", 98394, "Sales", "Salesperson", 20000, 26, date(1998, 12, 7), "DEF54321", 15000, sales_manager2)
  sales_manager1.manages.extend([salesperson1, salesperson2])
  sales_manager2.manages.extend([salesperson3])
  
 #create clients
  client1 = Client(1, "Anood Mohammed", "Dalma St", "Anood.Mohammed@gmail.com", 5000)
  client2 = Client(2, "Salem Saeed", "Al Mireef St", "Salem.Saeed@yahoo.com", 10000)

#create guests
  guest1 = Guest(1, "Sara Ali", "Channel St", "Sara.Alid@yahoo.com")
  guest2 = Guest(2, "Hamad Aref", "Al Maha St", "Hamad.Aref@gmail.com")

#create suppliers
  catering_company = CateringCompany(1, "Sun Catering", "17th St", "Sun.Catering@yahoo.com", ["Menu Item 1", "Menu Item 2"])
  cleaning_company = CleaningCompany(2, "Luck Catering", "10th St", "Luck.Catering@yahoo.com")
  decorations_company = DecorationsCompany(3, "Moonlight Decorations", "11th St", "decorations@gmail.com")
  entertainment_company = EntertainmentCompany(4, "Entertainment Co.", "16th St", "entertainment@gmail.com")
  furniture_supply_company = FurnitureSupplyCompany(5, "Cloud Furniture", "12th St", "Cloud.furniture@gmail.com")
  
# Create venue
  venue = Venue(1, "Event Hall", "Al Asayil St", "venue@yahoo.com", 50, 100)

# Create event
  event = Event(1, "Wedding", "Garden Theme", date(2024, 5, 10), time(18, 0), 4, "Matar Bin Thani St", client1, [guest1, guest2])
  event.suppliers.extend([catering_company, cleaning_company, decorations_company, entertainment_company, furniture_supply_company])

#print event details
  print("Event Details: ")
  print("Event ID: ", event.eventID)
  print("Event Type:", event.eventType)
  print("Theme:", event.theme)
  print("Date:", event.date)
  print("Time:", event.time)
  print("Duration:", event.duration)
  print("Venue Address:", event.venueAddress)
  print("Client:", event.client.name)
  print("Guests:")
  for guest in event.guests:
    print("-", guest.name)
  print("Suppliers:")
  for supplier in event.suppliers:
    print("-", supplier.name)

            




























