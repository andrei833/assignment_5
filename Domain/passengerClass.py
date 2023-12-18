class Passenger():
    def __init__(self,first_name,last_name,passport_nr):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__passport_nr = passport_nr

    def __str__(self) -> str:
        return (f"The passanger {self.__first_name} {self.__last_name} has the passport number {self.__passport_nr}.")
    
    def __repr__(self) -> str:
        return (f"{self.__first_name} {self.__last_name}")

    # Getters
    def get_first_name(self):
        """
        D: Retrieves the first name of the passenger.
        I: None
        O: Returns the first name of the passenger.
        """
        return self.__first_name

    def get_last_name(self):
        """
        D: Retrieves the last name of the passenger.
        I: None
        O: Returns the last name of the passenger.
        """
        return self.__last_name

    def get_passport_nr(self):
        """
        D: Retrieves the passport number of the passenger.
        I: None
        O: Returns the passport number of the passenger.
        """
        return self.__passport_nr

    # Setters
    def set_first_name(self, new_first_name):
        """
        D: Sets a new first name for the passenger.
        I: new_first_name (str) - The new first name to set.
        O: None
        """
        self.__first_name = new_first_name

    def set_last_name(self, new_last_name):
        """
        D: Sets a new last name for the passenger.
        I: new_last_name (str) - The new last name to set.
        O: None
        """
        self.__last_name = new_last_name

    def set_passport_nr(self, new_passport_nr):
        """
        D: Sets a new passport number for the passenger.
        I: new_passport_nr (str) - The new passport number to set.
        O: None
        """
        self.__passport_nr = new_passport_nr
