from passengerClass import Passenger

class Plane():
    def __init__(self,id,airlane,nr_seats,destination,passengers):
        self.__id = id
        self.__airline = airlane
        self.__nr_seats = nr_seats
        self.__destination = destination
        self.__passengers = passengers =[
            Passenger("Ian","Lee","242"),
            Passenger("Tim","John",1273),
            Passenger("Alice","Smith",1573)
        ]

    def __str__(self):
        return (f"Plane {self.__id} airline company {self.__airline} with {self.__nr_seats} seats flying to {self.__destination} with the passengers {self.__passengers}.")
    
    #getters
    def get_id(self):
        return self.__id
    
    def get_airline(self):
        return self.__airline
    
    def get_nr_seats(self):
        return self.__nr_seats
    
    def get_destination(self):
        return self.__destination
    
    def get_list_of_passengers(self):
        return self.__passengers
    
    #setters
    def set_id(self,new_id):
        self.__id =  new_id

    def set_airline(self,new_airline):
        self.__airline = new_airline

    def set_nr_seats(self,new_number):
        self.__nr_seats = new_number

    def set_destination(self,new_destination):
        self.__destination = new_destination

    def set_passengers(self,new_passengers):
        self.__passengers = new_passengers

    def add_passenger(self,passenger):
        self.__passengers.append(passenger)