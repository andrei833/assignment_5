class Ui():
    def __init__(self,repo):
        self.__repo = repo

    def menu(self):
        s = "Menu:\n"
        s += "1) Get all airplanes\n"
        s += ""
        print(s)
    
    def Start(self):
        alive = True
        while(alive):

            self.menu()
            command = input("")
            
            if command is "0":
                alive = False
            elif command is "1":
                self.__repo.get_planes()
            else: print("Wrong command! Retry!")
