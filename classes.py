from datetime import datetime

class Hotel:
    """Represents a hotel with basic information and lists of rooms and employees."""
    def __init__(self, name, location, rating, total_rooms):
        """Initializes a new Hotel object."""
        self.name = name  # Hotel name
        self.location = location  # Hotel location
        self.rating = rating  # Hotel rating (e.g., number of stars)
        self.total_rooms = total_rooms  # Total number of rooms in the hotel
        self.roomList = []  # List to store Room objects
        self.employeeList = []  # List to store Employee objects

    def getName(self):
        """Returns the name of the hotel."""
        return self.name

    def setName(self, name):
        """Sets the name of the hotel."""
        self.name = name

    def getLocation(self):
        """Returns the location of the hotel."""
        return self.location

    def getRating(self):
        """Returns the rating of the hotel."""
        return self.rating

    def setRating(self, rating):
        """Sets the rating of the hotel."""
        self.rating = rating

    def getTotalRooms(self):
        """Returns the total number of rooms in the hotel."""
        return self.total_rooms

    def setTotalRooms(self, total_rooms):
        """Sets the total number of rooms in the hotel."""
        self.total_rooms = total_rooms

    def add_room(self, room):
        """Adds a Room object to the hotel's roomList."""
        self.roomList.append(room)

    def add_staff(self, staff):
        """Adds an Employee object to the hotel's employeeList."""
        self.employeeList.append(staff)

    def __str__(self):
        """Returns a string representation of the Hotel object."""
        return f"Hotel(name={self.name}, location={self.location}, rating={self.rating}, total_rooms={self.total_rooms})"


class Room:
    """Represents a hotel room with its attributes and availability status."""
    def __init__(self, room_number, room_type, amenities, price_per_night, availability_status=True):
        """Initializes a new Room object."""
        self.room_number = room_number  # Unique room number
        self.room_type = room_type  # Type of room (e.g., Standard, Deluxe)
        self.amenities = amenities  # List of amenities available in the room
        self.price_per_night = price_per_night  # Price per night for the room
        self.availability_status = availability_status  # Boolean indicating room availability

    def get_room_number(self):
        """Returns the room number."""
        return self.room_number

    def set_room_number(self, room_number):
        """Sets the room number."""
        self.room_number = room_number

    def get_room_type(self):
        """Returns the room type."""
        return self.room_type

    def set_room_type(self, room_type):
        """Sets the room type."""
        self.room_type = room_type

    def get_amenities(self):
        """Returns the list of amenities."""
        return self.amenities

    def set_amenities(self, amenities):
        """Sets the list of amenities."""
        self.amenities = amenities

    def get_price_per_night(self):
        """Returns the price per night."""
        return self.price_per_night

    def set_price_per_night(self, price_per_night):
        """Sets the price per night."""
        self.price_per_night = price_per_night

    def get_availability_status(self):
        """Returns the availability status."""
        return self.availability_status

    def set_availability_status(self, availability_status):
        """Sets the availability status."""
        self.availability_status = availability_status

    def __str__(self):
        """Returns a string representation of the Room object."""
        return f"Room(room_number={self.room_number}, room_type={self.room_type}, price_per_night={self.price_per_night}, availability={self.availability_status})"


class Employee:
    """Base class for all hotel employees."""
    def __init__(self, employee_id, name, position, salary):
        """Initializes a new Employee object."""
        self.employee_id = employee_id  # Unique employee ID
        self.name = name  # Employee name
        self.position = position  # Employee job position
        self.salary = salary  # Employee salary

    def get_employee_id(self):
        """Returns the employee ID."""
        return self.employee_id

    def set_employee_id(self, employee_id):
        """Sets the employee ID."""
        self.employee_id = employee_id

    def get_name(self):
        """Returns the employee name."""
        return self.name

    def set_name(self, name):
        """Sets the employee name."""
        self.name = name

    def get_position(self):
        """Returns the employee position."""
        return self.position

    def set_position(self, position):
        """Sets the employee position."""
        self.position = position

    def get_salary(self):
        """Returns the employee salary."""
        return self.salary

    def set_salary(self, salary):
        """Sets the employee salary."""
        self.salary = salary

    def __str__(self):
        """Returns a string representation of the Employee object."""
        return f"Employee(id={self.employee_id}, name={self.name}, position={self.position})"


class Manager(Employee):
    """Represents a manager with additional department information."""
    def __init__(self, employee_id, name, position, salary, department, team_size):
        """Initializes a new Manager object."""
        super().__init__(employee_id, name, position, salary)  # Call to the parent class (Employee) constructor
        self.department = department  # Department the manager is responsible for
        self.team_size = team_size  # Number of employees in the manager's team

    def get_department(self):
        """Returns the department."""
        return self.department

    def set_department(self, department):
        """Sets the department."""
        self.department = department

    def get_team_size(self):
        """Returns the team size."""
        return self.team_size

    def set_team_size(self, team_size):
        """Sets the team size."""
        self.team_size = team_size

    def __str__(self):
        """Returns a string representation of the Manager object."""
        return f"Manager(name={self.name}, department={self.department}, team_size={self.team_size})"


class Receptionist(Employee):
    """Represents a receptionist with shift and language skills."""
    def __init__(self, employee_id, name, position, salary, shift, language_skills):
        """Initializes a new Receptionist object."""
        super().__init__(employee_id, name, position, salary)  # Call to the parent class (Employee) constructor
        self.shift = shift  # Shift of the receptionist (e.g., Morning, Afternoon)
        self.language_skills = language_skills  # List of languages the receptionist speaks

    def get_shift(self):
        """Returns the shift."""
        return self.shift

    def set_shift(self, shift):
        """Sets the shift."""
        self.shift = shift

    def get_language_skills(self):
        """Returns the list of language skills."""
        return self.language_skills

    def set_language_skills(self, language_skills):
        """Sets the list of language skills."""
        self.language_skills = language_skills

    def __str__(self):
        """Returns a string representation of the Receptionist object."""
        return f"Receptionist(name={self.name}, shift={self.shift}, languages={self.language_skills})"


class Guest:
    """Represents a hotel guest with personal information."""
    def __init__(self, guest_id, name, contact_info, loyalty_status="Basic"):
        """Initializes a new Guest object."""
        self.guest_id = guest_id  # Unique guest ID
        self.name = name  # Guest name
        self.contact_info = contact_info  # Guest contact information (e.g., email, phone)
        self.loyalty_status = loyalty_status  # Guest loyalty status (e.g., Basic, Silver, Gold)
        self.bookingList = []  # List to store Booking objects
        self.LoyaltyprogramList = []  #List to store loyalty programs

    def get_guest_id(self):
        """Returns the guest ID."""
        return self.guest_id

    def set_guest_id(self, guest_id):
        """Sets the guest ID."""
        self.guest_id = guest_id

    def get_name(self):
        """Returns the guest name."""
        return self.name

    def set_name(self, name):
        """Sets the guest name."""
        self.name = name

    def get_contact_info(self):
        """Returns the guest contact information."""
        return self.contact_info

    def set_contact_info(self, contact_info):
        """Sets the guest contact information."""
        self.contact_info = contact_info

    def get_loyalty_status(self):
        """Returns the guest loyalty status."""
        return self.loyalty_status

    def set_loyalty_status(self, loyalty_status):
        """Sets the guest loyalty status."""
        self.loyalty_status = loyalty_status

    def add_reservation(self, booking):
        """Adds a Booking object to the guest's bookingList."""
        self.bookingList.append(booking)

    def __str__(self):
        """Returns a string representation of the Guest object."""
        return f"Guest(id={self.guest_id}, name={self.name}, status={self.loyalty_status})"


class Booking:
    """Represents a booking made by a guest for a specific room."""
    def __init__(self, booking_id, guest, room, check_in_date, check_out_date):
        """Initializes a new Booking object."""
        self.booking_id = booking_id  # Unique booking ID
        self.guest = guest  # Guest object associated with the booking
        self.room = room  # Room object associated with the booking
        self.check_in_date = check_in_date  # Check-in date
        self.check_out_date = check_out_date  # Check-out date
        self.paymentList = []  #List of payment
        self.invoiceList = []  # List of invoices

    def get_booking_id(self):
        """Returns the booking ID."""
        return self.booking_id

    def set_booking_id(self, booking_id):
        """Sets the booking ID."""
        self.booking_id = booking_id

    def get_guest(self):
        """Returns the Guest object."""
        return self.guest

    def set_guest(self, guest):
        """Sets the Guest object."""
        self.guest = guest

    def get_room(self):
        """Returns the Room object."""
        return self.room

    def set_room(self, room):
        """Sets the room."""
        self.room = room

    def get_check_in_date(self):
        """Returns the check-in date."""
        return self.check_in_date

    def set_check_in_date(self, check_in_date):
        """Sets the check-in date."""
        self.check_in_date = check_in_date

    def get_check_out_date(self):
        """Returns the check-out date."""
        return self.check_out_date

    def set_check_out_date(self, check_out_date):
        """Sets the check-out date."""
        self.check_out_date = check_out_date

    def __str__(self):
        """Returns a string representation of the Booking object."""
        return f"Booking(id={self.booking_id}, guest={self.guest.get_name()}, room={self.room.get_room_number()})"


class Invoice:
    """Represents an invoice for a booking."""
    def __init__(self, invoice_id, booking, total_amount, issue_date):
        """Initializes a new Invoice object."""
        self.invoice_id = invoice_id  # Unique invoice ID
        self.booking = booking  # Booking object associated with the invoice
        self.total_amount = total_amount  # Total amount due
        self.issue_date = issue_date  # Date the invoice was issued

    def get_invoice_id(self):
        """Returns the invoice ID."""
        return self.invoice_id

    def set_invoice_id(self, invoice_id):
        """Sets the invoice ID."""
        self.invoice_id = invoice_id

    def get_booking(self):
        """Returns the Booking object."""
        return self.booking

    def set_booking(self, booking):
        """Sets the booking."""
        self.booking = booking

    def get_total_amount(self):
        """Returns the total amount."""
        return self.total_amount

    def set_total_amount(self, total_amount):
        """Sets the total amount."""
        self.total_amount = total_amount

    def get_issue_date(self):
        """Returns the issue date."""
        return self.issue_date

    def set_issue_date(self, issue_date):
        """Sets the issue date."""
        self.issue_date = issue_date

    def __str__(self):
        """Returns a string representation of the Invoice object."""
        return f"Invoice(id={self.invoice_id}, amount={self.total_amount}, date={self.issue_date})"


class Payment:
    """Represents a payment made for a booking."""
    def __init__(self, payment_id, booking, amount, payment_method):
        """Initializes a new Payment object."""
        self.payment_id = payment_id  # Unique payment ID
        self.booking = booking  # Booking object associated with the payment
        self.amount = amount  # Payment amount
        self.payment_method = payment_method  # Payment method (e.g., Credit Card, Cash)

    def get_payment_id(self):
        """Returns the payment ID."""
        return self.payment_id

    def set_payment_id(self, payment_id):
        """Sets the payment ID."""
        self.payment_id = payment_id

    def get_booking(self):
        """Returns the Booking object."""
        return self.booking

    def set_booking(self, booking):
        """Sets the booking."""
        self.booking = booking

    def get_amount(self):
        """Returns the payment amount."""
        return self.amount

    def set_amount(self, amount):
        """Sets the payment amount."""
        self.amount = amount

    def get_payment_method(self):
        """Returns the payment method."""
        return self.payment_method

    def set_payment_method(self, payment_method):
        """Sets the payment method."""
        self.payment_method = payment_method

    def process_payment(self):
        """Simulates payment processing (in a real system, this would involve actual payment gateway integration)."""
        # Payment processing logic would go here
        return True

    def __str__(self):
        """Returns a string representation of the Payment object."""
        return f"Payment(id={self.payment_id}, amount={self.amount}, method={self.payment_method})"


class LoyaltyProgram:
    """Represents a loyalty program for guests."""
    def __init__(self, program_id, program_name, points_balance=0, tier_level="Basic"):
        """Initializes a new LoyaltyProgram object."""
        self.program_id = program_id  # Unique program ID
        self.program_name = program_name  # Program name
        self.points_balance = points_balance  # Points balance
        self.tier_level = tier_level  # Tier level

    def getProgramId(self):
        """Returns the program ID."""
        return self.program_id

    def setProgramId(self, program_id):
        """Sets the program ID."""
        self.program_id = program_id

    def getProgramName(self):
        """Returns the program name."""
        return self.program_name

    def setProgramName(self, program_name):
        """Sets the program name."""
        self.program_name = program_name

    def getPointsBalance(self):
        """Returns the points balance."""
        return self.points_balance

    def setPointsBalance(self, points_balance):
        """Sets the points balance."""
        self.points_balance = points_balance

    def getTierLevel(self):
        """Returns the tier level."""
        return self.tier_level

    def setTierLevel(self, tier_level):
        """Sets the tier level."""
        self.tier_level = tier_level

    def earnPoints(self, amount):
        """Earn points and update tier level."""
        self.points_balance += amount
        # Update tier based on points
        if self.points_balance >= 10000:
            self.tier_level = "Platinum"
        elif self.points_balance >= 5000:
            self.tier_level = "Gold"
        elif self.points_balance >= 1000:
            self.tier_level = "Silver"

    def redeemPoints(self, points):
        """Redeem points."""
        if points > self.points_balance:
            return False
        self.points_balance -= points
        return True

    def __str__(self):
        """Returns a string representation of the LoyaltyProgram object."""
        return f"LoyaltyProgram(name={self.program_name}, points={self.points_balance}, tier={self.tier_level})"


class ServiceRequest:
    """Represents a service request from a guest."""
    def __init__(self, request_id, guest, request_type, description, status="Pending"):
        """Initializes a new ServiceRequest object."""
        self.request_id = request_id  # Unique request ID
        self.guest = guest  # Guest object associated with the request
        self.request_type = request_type  # Type of service requested (e.g., Housekeeping, Maintenance)
        self.description = description  # Description of the service request
        self.status = status  # Status of the service request (e.g., Pending, In Progress, Completed)
        self.created_at = datetime.now()  #Time of creation

    def getRequestId(self):
        """Returns the request ID."""
        return self.request_id

    def setRequestId(self, request_id):
        """Sets the request ID."""
        self.request_id = request_id

    def getGuest(self):
        """Returns the Guest object."""
        return self.guest

    def setGuest(self, guest):
        """Sets the guest."""
        self.guest = guest

    def getRequestType(self):
        """Returns the request type."""
        return self.request_type

    def setRequestType(self, request_type):
        """Sets the request type."""
        self.request_type = request_type

    def getDescription(self):
        """Returns the description."""
        return self.description

    def setDescription(self, description):
        """Sets the description."""
        self.description = description

    def getStatus(self):
        """Returns the status."""
        return self.status

    def setStatus(self, status):
        """Sets the status."""
        self.status = status

    def updateStatus(self, status):
        """Updates the status."""
        self.status = status

    def __str__(self):
        """Returns a string representation of the ServiceRequest object."""
        return f"ServiceRequest(id={self.request_id}, type={self.request_type}, status={self.status})"


class Feedback:
    """Represents feedback from a guest about their stay."""
    def __init__(self, feedback_id, guest, rating, comments, date_submitted=None):
        """Initializes a new Feedback object."""
        self.feedback_id = feedback_id  # Unique feedback ID
        self.guest = guest  # Guest object associated with the feedback
        self.rating = rating  # Rating given by the guest (e.g., 1-5 stars)
        self.comments = comments  # Additional comments from the guest
        self.date_submitted = datetime.now() #Date of submission

    def getFeedbackId(self):
        """Returns the feedback ID."""
        return self.feedback_id

    def setFeedbackId(self, feedback_id):
        """Sets the feedback ID."""
        self.feedback_id = feedback_id

    def getGuest(self):
        """Returns the Guest object."""
        return self.guest

    def setGuest(self, guest):
        """Sets the guest."""
        self.guest = guest

    def getRating(self):
        """Returns the rating."""
        return self.rating

    def setRating(self, rating):
        """Sets the rating."""
        if 1 <= rating <= 5:
            self.rating = rating
        else:
            raise ValueError("Rating must be between 1 and 5")

    def getComments(self):
        """Returns the comments."""
        return self.comments

    def setComments(self, comments):
        """Sets the comments."""
        self.comments = comments

    def getDateSubmitted(self):
        """Returns the date submitted."""
        return self.date_submitted

    def setDateSubmitted(self, date_submitted):
        """Sets the date submitted."""
        self.date_submitted = date_submitted

    def displayFeedback(self):
        """Displays the feedback."""
        return f"Feedback from {self.guest.get_name()} on {self.date_submitted}: {self.rating}/5 - {self.comments}"

    def __str__(self):
        """Returns a string representation of the Feedback object."""
        return f"Feedback(id={self.feedback_id}, rating={self.rating}, date={self.date_submitted})"


# Example Usage (Test Case)
if __name__ == '__main__':
    # Create a hotel
    hotel = Hotel("Grand View Hotel", "Mountain View", 5, 150)
    print("Created hotel:", hotel)

    # Create rooms
    room1 = Room("101", "Standard", ["TV", "AC", "Wi-Fi"], 120)
    print("Created room1:", room1)
    room2 = Room("201", "Deluxe", ["TV", "AC", "Wi-Fi", "Balcony"], 200)
    print("Created room2:", room2)
    hotel.add_room(room1)
    hotel.add_room(room2)
    print("Added rooms to hotel")

    # Create employees
    manager = Manager("M001", "David Miller", "General Manager", 6000, "Operations", 12)
    print("Created manager:", manager)
    receptionist = Receptionist("R001", "Emily White", "Front Desk Agent", 3000, "Afternoon", ["English", "Spanish"])
    print("Created receptionist:", receptionist)
    hotel.add_staff(manager)
    hotel.add_staff(receptionist)
    print("Added staff to hotel")

    # Create guests
    guest1 = Guest("G001", "Sophia Rodriguez", "sophia@email.com")
    print("Created guest1:", guest1)
    guest2 = Guest("G002", "Liam Johnson", "liam@email.com")
    print("Created guest2:", guest2)

    # Create loyalty program
    loyalty_program = LoyaltyProgram("LP001", "Premium Rewards")
    print("Created loyalty program:", loyalty_program)
    guest1.LoyaltyprogramList.append(loyalty_program)
    print("Added loyalty program to guest1")

    # Create bookings
    booking1 = Booking("B001", guest1, room1, "2025-04-01", "2025-04-04")
    print("Created booking1:", booking1)

    booking2 = Booking("B002", guest2, room2, "2025-04-06", "2025-04-09")
    print("Created booking2:", booking2)

    # Process payments
    payment1 = Payment("P001", booking1, 360, "Credit Card")
    print("Created payment1:", payment1)
    payment2 = Payment("P002", booking2, 600, "Cash")
    print("Created payment2:", payment2)

    # Create invoices
    invoice1 = Invoice("I001", booking1, 360, "2025-03-30")
    print("Created invoice1:", invoice1)
    invoice2 = Invoice("I002", booking2, 600, "2025-03-30")
    print("Created invoice2:", invoice2)

    # Add service request
    service_request = ServiceRequest("SR001", guest1, "Maintenance", "Leaky faucet in bathroom")
    print("Created service request:", service_request)

    # Add feedback
    feedback = Feedback("F001", guest2, 4, "Comfortable stay, but breakfast was limited")
    print("Created feedback:", feedback)

    # Simulate loyalty program points earning
    loyalty_program.earnPoints(500)
    print("Loyalty Program after earning points:", loyalty_program)

    # Update service request status
    service_request.updateStatus("Completed")
    print("Updated Service Request:", service_request)

    # Display feedback
    print("Feedback Display:", feedback.displayFeedback())
