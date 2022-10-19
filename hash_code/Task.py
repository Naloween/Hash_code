
from hash_code.ObjectsStructure import Engineer, Service, Binary, Feature

class Task:
    def __init__(self, engineer: Engineer, time: int, nb_of_days: int):
        self.engineer: Engineer = engineer
        self.time = time
        self.nb_of_days: int = nb_of_days
    
    def toString(self):
        return "this function has not been implemented"

class ImplementFeature(Task):
    def __init__(self, engineer: Engineer, time: int, feature: Feature, binary: Binary):

        Task.__init__(self, engineer, time, feature.difficulty + len(binary.services) + binary.get_nb_engineer_working(time))
        
        self.feature: Feature = feature
        self.binary: Binary = binary
    
    def toString(self):
        return "impl " + self.feature.name + " " + str(self.binary.id)

class MoveService(Task):
    def __init__(self, engineer: Engineer, time: int, service: Service, binary: Binary):
        Task.__init__(self, engineer, time, max(len(service.binary.services), len(binary.services)))

        self.service: Service = service
        self.binary: Binary = binary
    
    def toString(self):
        return "move " + self.service.name + " " + str(self.service.binary.id) + " " + str(self.binary.id)

class CreateEmptyBinary(Task):

    nb_of_days = 1

    def __init__(self, engineer: Engineer, time: int):
        Task.__init__(self, engineer, time, CreateEmptyBinary.nb_of_days)
    
    def toString(self):
        return "new"

class Wait(Task):
    def __init__(self, engineer: Engineer, time: int, nb_days):
        Task.__init__(self, engineer, time, nb_days)
    
    def toString(self):
        return "wait " + str(self.nb_of_days)
