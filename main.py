from Infrastructure.planeRepository import PlaneRepository
from UserInterface.userInterface import Ui
from test import tests


if __name__ == "__main__":
    tests()
    repo = PlaneRepository()
    ui = Ui(repo)
    ui.Start()