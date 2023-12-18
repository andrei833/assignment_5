from planeClass import Plane
from passengerClass import Passenger
from logic import sortalg

class PlaneRepository():
    def __init__(self):
        self.__data = [Plane(12,"Wiz",23,"Beijing"),
                       Plane(1,"R_Air",43,"NewYork"),
                       Plane(1,"Airbuss",11,"France")]

    def __str__(self):
        return f"There are {len(self.__data)} airplanes."
    
    # Getters
    def get_planes(self):
        """
        D: Retrieves the list of airplanes.
        I: None
        O: Returns the list of airplanes.
        """
        return self.__data

    def get_plane_index(self, index):
        """
        D: Retrieves a specific airplane from the list by index.
        I: index (int) - The index of the airplane to retrieve.
        O: Returns the airplane at the specified index.
        """
        return self.__data[index]

    # Setters
    def set_planes(self, plane_list):
        """
        D: Sets a new list of airplanes.
        I: plane_list (list) - The new list of airplanes.
        O: None
        """
        self.__data = plane_list

    def add_plane(self, plane):
        """
        D: Adds a new airplane to the list.
        I: plane - The airplane object to add.
        O: None
        """
        self.__data.append(plane)

    def add_passenger_to_plane(self, index, passenger):
        """
        D: Adds a new passenger to a specific airplane.
        I: index (int) - The index of the airplane.
        passenger - The passenger object to add.
        O: None
        """
        self.__data[index].add_passenger(passenger)

    def sort_passengers_plane(self, index):
        """
        D: Sorts the passengers of a specific airplane based on last names.
        I: index (int) - The index of the airplane.
        O: None
        """
        plane = self.get_plane_index(index)
        passengers = plane.get_list_of_passengers()
        passengers = sortalg(passengers, lambda x, y: x.get_last_name() < y.get_last_name())
        plane.set_passengers(passengers)
        self.__data[index] = plane

    def sort_planes_nr(self):
        """
        D: Sorts the airplanes based on the number of passengers.
        I: None
        O: None
        """
        self.__data = sortalg(self.__data, lambda x, y: x.get_nr_of_passengers() < y.get_nr_of_passengers())

    def sort_planes_nr_first_name(self, first_name):
        """
        D: Sorts the airplanes based on the number of passengers with a specific first name.
        I: first_name (str) - The first name to consider.
        O: None
        """
        self.__data = sortalg(self.__data, lambda x, y: x.get_nr_of_passengers_with_first_name(first_name) < y.get_nr_of_passengers_with_first_name(first_name))

    def sort_planes_concat_nr_and_dest(self):
        """
        D: Sorts the airplanes based on the concatenation of the number of passengers and destination.
        I: None
        O: None
        """
        self.__data = sortalg(self.__data, lambda x, y: x.concat() < y.concat())

    def get_planes_passport_nr_same_letters(self):
        """
        D: Retrieves airplanes with passengers having passport numbers with the same letters.
        I: None
        O: Returns a list of airplanes.
        """
        planes = []
        for p in self.__data:
            ok = 0
            passengers = p.get_list_of_passengers()
            for pas in passengers:
                nr = pas.get_passport_nr()
                if nr[0] == nr[1] == nr[2]:
                    ok = 1
            if ok:
                planes.append(p)
        return planes

    def get_passenger_string_plane(self, index, string):
        """
        D: Retrieves passengers from a specific airplane whose first name or last name contains a specific string.
        I: index (int) - The index of the airplane.
        string (str) - The string to search for in passengers' names.
        O: Returns a list of passengers.
        """
        people = []
        all_people = self.get_plane_index(index).get_list_of_passengers()
        for passenger in all_people:
            if string in passenger.get_first_name() or string in passenger.get_last_name():
                people.append(passenger)
        return people

    def get_planes_by_name(self, first, last):
        """
        D: Retrieves airplanes with passengers having a specific first name and last name.
        I: first (str) - The first name to search for.
        last (str) - The last name to search for.
        O: Returns a list of airplanes.
        """
        planes = []
        for p in self.__data:
            ok = 0
            passengers = p.get_list_of_passengers()
            for pas in passengers:
                if pas.get_first_name() == first and pas.get_last_name() == last:
                    ok = 1
            if ok:
                planes.append(p)
        return planes

    
    
    
#repo = PlaneRepository()
#people = repo.get_passenger_string_plane(0,"i")
#print(people)