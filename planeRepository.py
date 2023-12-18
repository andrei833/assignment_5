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
    
    #getters
    def get_planes(self):
        return self.__data
    
    def get_plane_index(self,index):
        return self.__data[index]
    
    #setters
    def set_planes(self,list):
        self.__data = list
    
    def add_plane(self,plane):
        self.__data.append(plane)

    def add_passenger_to_plane(self,index,passenger):
        self.__data[index].add_passenger(passenger)

    def sort_passengers_plane(self,index):
        plane = self.get_plane_index(index)
        passengers = plane.get_list_of_passengers()
        passengers = sortalg(passengers,lambda x,y: x.get_last_name() < y.get_last_name())
        plane.set_passengers(passengers)
        self.__data[index] = plane

    def sort_planes_nr(self):
        self.__data = sortalg(self.__data,lambda x,y: x.get_nr_of_passengers() < y.get_nr_of_passengers())

    def sort_planes_nr_first_name(self,first_name):
        self.__data = sortalg(self.__data,lambda x,y: x.get_nr_of_passengers_with_first_name(first_name) < y.get_nr_of_passengers_with_first_name(first_name))

    def sort_planes_concat_nr_and_dest(self):
        self.__data = sortalg(self.__data,lambda x,y: x.concat() < y.concat())

    def get_planes_passport_nr_same_letters(self):
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

    def get_passenger_string_plane(self,index,string):
        people = []
        all_people = self.get_plane_index(index).get_list_of_passengers()
        print (all_people)
        for passenger in all_people:
            if string in passenger.get_first_name() or string in passenger.get_last_name():
                people.append(passenger)
        return people

    def get_planes_by_name(self,first,last):
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