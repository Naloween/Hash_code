
from Engineer import Engineer
from Task import Task, ImplementFeature, MoveService, CreateEmptyBinary, Wait

class Schedule:
    def __init__(self, nb_engineers):
        self.engineers: list[Engineer] = [Engineer() for k in range(nb_engineers)]
