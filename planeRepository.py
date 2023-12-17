from planeClass import Plane
from logic import sortalg

class PlaneRepository():
    def __init__(self):
        self.__data = [Plane(12,"d",23,"cHINA")]

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

    def sort_passangers_plane(self,index):
        plane = self.get_plane_index(index)
        passangers = plane.get_list_of_passengers()
        passangers = sortalg(passangers,lambda x,y: x.get_last_name() < y.get_last_name())
        plane.set_passengers(passangers)
        self.__data[index] = plane
