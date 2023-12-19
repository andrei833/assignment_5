class Ui():
    def __init__(self,repo):
        self.__repo = repo

    def menu(self):
        s = "Menu:\n"
        s += "1) Get all airplanes.\n"
        s += "2) Get plane by index.\n"
        
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
                self.__repo.sort_planes_concat_nr_and_dest()
            elif command == "6":
                self.ui_get_passangers_same_pasport_letters()
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

    def ui_get_passangers_same_pasport_letters(self):
        try:
            planes = self.__repo.get_planes_passport_nr_same_letters()
            for plane in planes:
                print (plane)
        except Exception as err:
            print(f"Error:{err}")