from planeRepository import PlaneRepository
from userInterface import Ui


if __name__ == "__main__":
    #tests()
    repo = PlaneRepository()
    ui = Ui(repo)
    ui.Start()