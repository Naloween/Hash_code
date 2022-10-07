
from ObjectsStructure import Engineer, Service, Binary, Feature

class Task:
    def __init__(self, engineer: Engineer, nb_of_days: int):
        self.engineer: Engineer = engineer
        self.nb_of_days: int = nb_of_days

class ImplementFeature(Task):
    def __init__(self, engineer: Engineer, feature: Feature, binary: Binary):

        Task.__init__(self, engineer, feature.difficulty + len(binary.services) + len(binary.engineers_working))
        
        self.feature: Feature = feature
        self.binary: Binary = binary

class MoveService(Task):
    def __init__(self, engineer: Engineer, service: Service, binary: Binary):
        Task.__init__(self, engineer, max(len(service.binary.services), len(binary.services)))

        self.service: Service = service
        self.binary: Binary = binary

class CreateEmptyBinary(Task):

    nb_of_days = 1

    def __init__(self, engineer: Engineer):
        Task.__init__(self, engineer, CreateEmptyBinary.nb_of_days)

class Wait(Task):
    def __init__(self, engineer: Engineer, nb_days):
        Task.__init__(self, engineer, nb_days)
