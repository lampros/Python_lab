class Person:
    """class Person is a parent class that represents a Person in general.
    """
    def __init__(self, name: str, age: int) -> None:
        """Initialize a person, which has a name and an age.

        Args:
            name (str): The person's name.
            age (int): The person's age.
        """
        self.name = name
        self.age = age

    def get_details(self) -> None:
        """This function prints the name and the age of the person.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Guest(Person):
    """class Guest is a subclass of class Person that represents a guest of the hotel.
    """
    def __init__(self, name: str, age: int, room_number: int, nights: int) -> None: 
        """Initialize a guest with the name, age, room number and number of nights that the guest will stay at the hotel.

        Args:
            name (str): The name of the guest.
            age (int): The age of the guest.
            room_number (int): The room number of the guest.
            nights (int): The number of nights that the guest will stay.
        """
        super().__init__(name, age)
        self.room_number = room_number
        self.nights = nights

    def calculate_bill(self, rate_per_night: float) -> float:
        """This function calculates the bill that the guest will pay, based on the rate per night.

        Args:
            rate_per_night (float): the room rate per night.

        Returns:
            float: the total bill based on the number of nights that the guest will stay and the rate per night. 
        """
        total_bill = self.nights * rate_per_night
        return total_bill

    def get_details(self) -> None:
        """This function calls the get_details function of parent class Person, and moreover prints the room number and the number of nights
         that the guest will stay at the hotel.
        """
        super().get_details()
        print(f"The guest will stay at {self.room_number} room for {self.nights} nights.")


class Staff(Person):
    """class Staff is a subclass of class Person that represents a staff member of the hotel.
    """
    def __init__(self, name: str, age: int, position: str, salary: float) -> None:
        """Initialize a staff member with a name, age, position, and salary. 

        Args:
            name (str): The name of the staff member.
            age (int): The age of the staff member.
            position (str): The position of the staff member. 
            salary (float): The salary of the staff member. 
        """
        super().__init__(name, age)
        self.position = position
        self.salary = salary

    def give_raise(self, amount: float) -> None:
        """This function increases the salary of the staff member by a specific amount.

        Args:
            amount (float): The amount added to the staff member's salary. 
        """
        self.salary += amount
        
    def get_details(self) -> None:
        """This function calls the get_details function of parent class Person, and moreover prints its current position and the earned salary. 
        """
        super().get_details()
        print(f"The Staff member is working as {self.position} and earns {self.salary} per month.") 


class Hotel:
    """This class represents the Management System of the Hotel. 
    """
    def __init__(self, name: str) -> None:
        """Initialize a hotel with a name.

        Args:
            name (str): The name of the hotel.
        """
        self.name = name
        self.guests: list[Guest] = []
        self.staff: list[Staff] = []

    def check_in(self, guest: Guest) -> None:
        """This function adds a guest to the hotel's guest list.

        Args:
            guest (Guest): A Guest object representing the guest to be added to the hotel.
        """
        self.guests.append(guest)

    def check_out(self, guest: Guest) -> None:
        """This function removes a guest from the hotel's list of guests.

        Args:
            guest (Guest): A Guest object representing the guest to be removed from the hotel.
        """
        self.guests.remove(guest)

    def hire_staff(self, staff_member: Staff) -> None:
        """This function adds a staff member to the hotel's list of staff members.

        Args:
            staff_member (Staff): A Staff object representing the staff member to be hired by the hotel.
        """
        self.staff.append(staff_member)

    def list_guests(self) -> None:
        """This function prints the details of all guests currently checked in at the hotel.
        """
        for guest in self.guests:
            guest.get_details()

    def list_staff(self) -> None:
        """This function prints the details of all staff members currently employed at the hotel.
        """
        for staff in self.staff:
            staff.get_details()


a_guest = Guest(name="Lampros", age=40, room_number=101, nights=5)
another_guest = Guest(name="Maria", age=35, room_number=401, nights=3)
a_staff_member = Staff(name="Georgia", age=40, position="Receptionist", salary=1000.0)
another_staff_member = Staff(name="Alexandra", age=30, position="Manager", salary=1500.0)
a_hotel = Hotel(name="Macedonia Palace")

a_hotel.check_in(a_guest)
a_hotel.check_in(another_guest)
a_hotel.hire_staff(a_staff_member)
a_hotel.hire_staff(another_staff_member)
a_hotel.check_out(a_guest)

a_staff_member.give_raise(200)

print("Final guest list:")
a_hotel.list_guests()

print("\nFinal staff list:")
a_hotel.list_staff()
