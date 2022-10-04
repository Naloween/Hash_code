
from Engineer import Engineer

class Task:
    def __init__(self, engineer: Engineer, nb_of_days: int):
        self.engineer: Engineer = engineer
        self.nb_of_days: int = nb_of_days

class ImplementFeature(Task):
    def __init__(self, engineer: Engineer):
        Task.__init__(self, engineer, 0)

class MoveService(Task):
    def __init__(self, engineer: Engineer):
        Task.__init__(self, engineer, 0)

class CreateEmptyBinary(Task):
    def __init__(self, engineer: Engineer):
        Task.__init__(self, engineer, 0)

class Wait(Task):
    def __init__(self, engineer: Engineer):
        Task.__init__(self, engineer, 0)
