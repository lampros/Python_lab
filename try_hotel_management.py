class Person:
    def __init__(self, name: str, age: int) ->None:
        self.name = name
        self.age = age

    def get_details(self) ->None:
        print(f"Name: {self.name} \nAge: {self.age}")


class Guest(Person):
    def __init__(self, name: str, age: int, room_number: int, nights: int) -> None:
        super().__init__(name, age)
        self.room_number = room_number
        self.nights = nights

    def calculate_bill(self, rate_per_night: float) -> float:
        return self.nights * rate_per_night

    def get_details(self) -> None:
        super().get_details()
        print(f"Room number: {self.room_number} \nNights: {self.nights}")

class Staff(Person):
    def __init__(self, name: str, age: int, position: str, salary: float) -> None:
        super().__init__(name, age)
        self.position = position
        self.salary = salary

    def give_raise(self, amount: float) -> None:
        self.salary += amount

    def get_details(self) -> None:
        super().get_details()
        print(f"Position: {self.position} \nSalary: {self.salary}")

class Hotel:
    def __init__(self, name: str) -> None:
        self.name = name
        self.guests: list[Guest] = []
        self.staff: list[Staff] = []

    def check_in(self, guest: Guest) -> None:
        self.guests.append(guest)

    def check_out(self, guest: Guest) -> None:
        self.guests.remove(guest)

    def hire_staff(self, staff_member: Staff) -> None:
        self.staff.append(staff_member)

    def list_guests(self) -> None:
        for guest in self.guests:
            guest.get_details()

    def list_staff(self) -> None:
        for staff in self.staff:
            staff.get_details()

a_guest = Guest(
    name="Lampros",
    age=40,
    room_number=101,
    nights=5
)

another_guest = Guest(
    name="Maria",
    age=35,
    room_number=401,
    nights=3
)

a_staff_member = Staff(
    name="Helen",
    age=40,
    position="Receptionist",
    salary=1000
)

another_staff_member = Staff(
    name="Katerina",
    age=30,
    position="Manager",
    salary=1200
)

a_hotel = Hotel(name="Macedonia Palace")

a_hotel.check_in(a_guest)
a_hotel.hire_staff(a_staff_member)
a_hotel.check_in(another_guest)
a_hotel.hire_staff(another_staff_member)

print("Current guests:")
a_hotel.list_guests()

print("\nCurrent staff:")
a_hotel.list_staff()

a_hotel.check_out(a_guest)
a_staff_member.give_raise(200)
