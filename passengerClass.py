class Passenger():
    def __init__(self,first_name,last_name,passport_nr):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__passport_nr = passport_nr

    def __str__(self) -> str:
        return (f"The passanger {self.__first_name} {self.__last_name} has the passport number {self.__passport_nr}.")
    
    def __repr__(self) -> str:
        return (f"{self.__first_name} {self.__last_name}")

    #getters
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_passport_nr(self):
        return self.__passport_nr
    
    #setters
    def set_first_name(self,new_first_name):
        self.__first_name = new_first_name

    def set_last_name(self,new_last_name):
        self.__last_name = new_last_name

    def set_passport_nr(self,new_passort_nr):
        self.__passport_nr = new_passort_nr