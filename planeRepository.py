class PlaneRepository():
    def __init__(self):
        self.__data = []

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