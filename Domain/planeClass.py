from Domain.passengerClass import Passenger

class Plane():
    def __init__(self,id,airlane,nr_seats,destination,passenger = [
            Passenger("Ian","Lee",242),
            Passenger("Tim","John",1273),
            Passenger("Alice","Smith",1573)
        ]):
        self.__id = id
        self.__airline = airlane
        self.__nr_seats = nr_seats
        self.__destination = destination
        self.__passengers = passenger

    def __str__(self):
        return (f"Plane {self.__id} airline company {self.__airline} with {self.__nr_seats} seats flying to {self.__destination} with the passengers {self.__passengers}.")
    
    def __repr__(self) -> str:
        return (f"Plane {self.__id} airline company {self.__airline} with {self.__nr_seats} seats flying to {self.__destination} with the passengers {self.__passengers}.")
    
    #getters
    def get_id(self):
        """
        D: Retrieves the unique identifier associated with the object.
        I: None
        O: Returns the unique identifier of the object.
        """
        return self.__id
    
    def get_airline(self):
        """
        D: Retrieves the airline associated with the object.
        I: None
        O: Returns the airline associated with the object.
        """
        return self.__airline

    
    def get_nr_seats(self):
        """
        D: Retrieves the number of seats available in the object.
        I: None
        O: Returns the number of seats available.
        """
        return self.__nr_seats

    def get_destination(self):
        """
        D: Retrieves the destination associated with the object.
        I: None
        O: Returns the destination of the object.
        """
        return self.__destination

    def get_list_of_passengers(self):
        """
        D: Retrieves the list of passengers associated with the object.
        I: None
        O: Returns the list of passengers.
        """
        return self.__passengers

    def get_nr_of_passengers(self):
        """
        D: Retrieves the number of passengers onboard.
        I: None
        O: Returns the number of passengers onboard.
        """
        return len(self.__passengers)

    
    def get_nr_of_passengers_with_first_name(self, first):
        """
        D: Retrieves the number of passengers with a specific first name.
        I: first (str) - The first name to search for.
        O: Returns the count of passengers with the specified first name.
        """
        passengers = self.__passengers
        count = 0
        for p in passengers:
            if first in p.get_first_name():
                count += 1
        return count

    def concat(self):
        """
        D: Concatenates the number of passengers and the destination.
        I: None
        O: Returns a string concatenation of the number of passengers and the destination.
        """
        return str(self.get_nr_of_passengers()) + self.get_destination()
    
    #setters
    def set_id(self, new_id):
        """
        D: Sets a new unique identifier for the object.
        I: new_id (str) - The new unique identifier to set.
        O: None
        """
        self.__id = new_id

    def set_airline(self, new_airline):
        """
        D: Sets a new airline for the object.
        I: new_airline (str) - The new airline to set.
        O: None
        """
        self.__airline = new_airline

    def set_nr_seats(self, new_number):
        """
        D: Sets a new number of seats for the object.
        I: new_number (int) - The new number of seats to set.
        O: None
        """
        self.__nr_seats = new_number

    def set_destination(self, new_destination):
        """
        D: Sets a new destination for the object.
        I: new_destination (str) - The new destination to set.
        O: None
        """
        self.__destination = new_destination

    def set_passengers(self, new_passengers):
        """
        D: Sets a new list of passengers for the object.
        I: new_passengers (list) - The new list of passengers to set.
        O: None
        """
        self.__passengers = new_passengers

    def add_passenger(self, passenger):
        """
        D: Adds a new passenger to the list of passengers.
        I: passenger - The passenger object to add.
        O: None
        """
        self.__passengers.append(passenger)
