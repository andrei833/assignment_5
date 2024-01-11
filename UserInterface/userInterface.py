class Ui():
    def __init__(self,repo):
        self.__repo = repo

    def menu(self):
        s = "Menu:\n"
        s += "1) Get all airplanes.\n"
        s += "2) Get plane by index.\n"
        s += "3) Sort the passengers in a plane by name.\n"
        s += "4) Sort planes according to the number of passengers.\n"
        s += "5) Sort planes according to the number of passengers with the first name starting with a given substring.\n"
        s += "6) Sort planes according to the string obtained by concatenation of the number ofpassengers in the plane and the destination.\n"
        s += "7) Identify planes that have passengers with passport numbers starting with the same 3 letters.\n"
        s += "8) Identify passengers from a given plane for which the first name or last name contain a string given as parameter.\n"
        s += "9) Identify plane/planes where there is a passenger with given name.\n"
        s += "10) Form groups of 𝒌 passengers from the same plane but with different last names (𝒌 is a value given by the user).\n"
        s += "11) Form groups of 𝒌 planes with the same destination but belonging to different airline companies (𝒌 is a value given by the user).\n"
        s += "0) Exit."
        print(s)
    
    def Start(self):
        alive = True
        while(alive):

            self.menu()
            command = input("")
            
            if command == "0":
                alive = False
            elif command == "1":
                for plane in self.__repo.get_planes():
                    print(plane)
            elif command == "2":
                self.ui_get_plane_by_index()
            elif command == "3":
                self.ui_sort_passengers_plane()
            elif command == "4":
                self.__repo.sort_planes_passenger_count()
            elif command == "5":
                self.__repo.sort_planes_nr_of_ppl_first_name("A")
            elif command == "6":
                self.__repo.sort_planes_concat_nr_and_dest()
            elif command == "7":
                self.ui_get_passangers_same_pasport_letters()
            elif command == "8":
                self.ui_get_passangers_from_plane_string()
            elif command == "9":
                self.ui_get_planes_passenger_name()
            elif command == "10":
                self.ui_get_k_people_same_plane_different_last_name()
            elif command == "11":
                self.ui_get_k_planes_same_destination_different_airline()
            else: print("Wrong command! Retry!")


    def get_index(self):
        try:
            index = int(input("Index:"))
            return index
        except Exception as err:
            print(f"Error:{err}")


    def ui_get_plane_by_index(self):
        try:
            index = self.get_index()
            print(self.__repo.get_plane_index(index))
        except Exception as err:
            print(f"Error:{err}")

    def ui_sort_passengers_plane(self):
        try:
            index = self.get_index()
            self.__repo.sort_passengers_plane(index)
        except Exception as err:
            print(f"Error:{err}")

    def ui_sort_planes_nr_of_ppl_first_name(self):
        try:
            first_name = input()
            self.__repo.sort_planes_nr_of_ppl_first_name(first_name)
        except Exception as err:
            print(f"Error:{err}")

    def ui_get_passangers_same_pasport_letters(self):
        try:
            planes = self.__repo.get_planes_passport_nr_same_letters()
            for plane in planes:
                print (plane)
        except Exception as err:
            print(f"Error:{err}")

    def ui_get_passangers_from_plane_string(self):
        try:
            index = self.get_index()
            string = input("String:")
            passengers = self.__repo.get_passenger_string_plane(index,string)
            for passenger in passengers:
                print (passenger)
        except Exception as err:
            print(f"Error:{err}")

    def ui_get_planes_passenger_name(self):
        try:
            first = input("First name:")
            last = input("Last name:")
            result = self.__repo.get_planes_by_name(first,last)
            if result is None:
                print ("There are no planes with passengers that have that name.")
            else:
                for r in result:
                    print(r)
        except Exception as err:
            print(f"Error:{err}")

    def ui_get_k_people_same_plane_different_last_name(self):
        try:
            k = int(input("k="))
            if k<2:
                raise Exception("K has to be greater than 1.")
            for plane in self.__repo.get_k_passengers_from_same_plane(k):
                print(plane)
        except Exception as err:
            print(f"Error:{err}")

    def ui_get_k_planes_same_destination_different_airline(self):
        try:
            k = int(input("k="))
            if k<2:
                raise Exception("K has to be greater than 1.")
            for plane in self.__repo.get_k_planes_same_plane_different_airlines(k):
                print(plane)
        except Exception as err:
            print(f"Error:{err}")