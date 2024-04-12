class Hotel:
    """
    Python class to implement a comprehensive hotel management system.

    This class encompasses functionalities for managing hotel rooms, employees, and guest reservations, 
    providing a foundational system for hotel operations.

    Syntax
    ------
    obj = Hotel(name)

    Parameters
    ----------
    [in] name : str
        The name of the hotel.

    Returns
    -------
    obj : Hotel
        An instance of the Hotel class, representing a single hotel with its management capabilities.

    Attributes
    ----------
    name : str
        The name of the hotel.
    rooms : list
        A list of Room instances representing the rooms available in the hotel.
    employees : list
        A list of Employee instances representing the employees working at the hotel.
    reservations : dict
        A dictionary mapping room numbers to guest names, representing current reservations.
    """
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.employees = []
        self.reservations = {}

    def add_room(self, room):
        self.rooms.append(room)

    def remove_room(self, room_number):
        for room in self.rooms:
            if room.get_room_number() == room_number:
                self.rooms.remove(room)
                print(f"Room {room_number} successfully removed from the hotel.")
                break
        else:
            print("Room not found in the hotel.")

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        for employee in self.employees:
            if employee.get_emp_id() == emp_id:
                self.employees.remove(employee)
                break
        else:
            print("Employee not found in the hotel.")

    def check_in(self, room_number, guest_name):
        room = self.find_room(room_number)
        if room is not None:
            if not room.is_occupied():
                room.check_in()
                self.reservations[room_number] = guest_name
                return f"Check-in successful for {guest_name} in room {room_number}."
            else:
                return "Room not available or already occupied."
        else:
            return "Room not found in the hotel."

    def check_out(self, room_number):
        room = self.find_room(room_number)
        if room is not None:
            if room.is_occupied():
                room.check_out()
                guest_name = self.reservations.pop(room_number, None)
                if guest_name:
                    return f"Check-out successful for {guest_name} from room {room_number}."
                else:
                    return "No guest found in the room."
            else:
                return "Room is not occupied."
        else:
            return "Room not found in the hotel."

    def find_room(self, room_number):
        for room in self.rooms:
            if room.get_room_number() == room_number:
                return room
        return None

class Room:
    """
    Python class to represent a hotel room.

    This class provides basic functionalities for managing hotel rooms.

    Syntax
    ------
    obj = Room(room_type, room_number, status, price)

    Parameters
    ----------
    [in] room_type : str
        The type or category of the room (e.g., 'Single', 'Double', 'Suite').
    [in] room_number : int
        The unique number or identifier of the room.
    [in] status : str
        The current status of the room (e.g., 'Occupied', 'Available', 'Under Maintenance').
    [in] price : float
        The price per night for the room.

    Returns
    -------
    obj : Room
        An instance of the Room class, representing a single hotel room.

    Attributes
    ----------
    room_type : str
        The type or category of the room.
    room_number : int
        The unique number or identifier of the room.
    status : str
        The current status of the room.
    price : float
        The price per night for the room.
    """
    def __init__(self, room_type, room_number, status, price):
        self.room_type = room_type
        self.room_number = room_number
        self.status = status
        self.price = price

    def get_room_number(self):
        return self.room_number

    def is_occupied(self):
        return self.status == "Occupied"

    def check_in(self):
        self.status = "Occupied"

    def check_out(self):
        self.status = "Available"

def main():
    # TESTING
    print("=================================================================")
    print("Test Case 1: Create a Hotel.")
    print("=================================================================")
    hotel = Hotel("Grand Hotel")
    if hotel.name == "Grand Hotel":
        print("Test PASS. The parameter name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    print("=================================================================")
    print("Test Case 2: Add a Room to the Hotel.")
    print("=================================================================")

    room1 = Room("Double", 101, "Available", 150)
    hotel.add_room(room1)

    if hotel.rooms[0] == room1:
        print("Test PASS. Room has been successfully added to the hotel.")
    else:
        print("Test FAIL. Check the method add_room().")

    print("=================================================================")
    print("Test Case 3: Remove a Room from the Hotel.")
    print("=================================================================")

    hotel.remove_room(101)
    if len(hotel.rooms) == 0:
        print("Test PASS. Room has been successfully removed from the hotel.")
    else:
        print("Test FAIL. Check the method remove_room().")

if __name__ == "__main__":
    main()
