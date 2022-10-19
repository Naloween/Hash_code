
from hash_code.ObjectsStructure import Engineer, Service, Binary, Feature

class Task:
    def __init__(self, engineer: Engineer, nb_of_days: int):
        self.engineer: Engineer = engineer
        self.nb_of_days: int = nb_of_days
    
    def toString(self):
        return "this function has not been implemented"

class ImplementFeature(Task):
    def __init__(self, engineer: Engineer, feature: Feature, binary: Binary):

        Task.__init__(self, engineer, feature.difficulty + len(binary.services) + len(binary.engineers_working))
        
        self.feature: Feature = feature
        self.binary: Binary = binary
    
    def toString(self):
        return "impl " + self.feature.name + " " + str(self.binary.id)

class MoveService(Task):
    def __init__(self, engineer: Engineer, service: Service, binary: Binary):
        Task.__init__(self, engineer, max(len(service.binary.services), len(binary.services)))

        self.service: Service = service
        self.binary: Binary = binary
    
    def toString(self):
        return "move " + self.service.name + " " + str(self.service.binary.id) + " " + str(self.binary.id)

class CreateEmptyBinary(Task):

    nb_of_days = 1

    def __init__(self, engineer: Engineer):
        Task.__init__(self, engineer, CreateEmptyBinary.nb_of_days)
    
    def toString(self):
        return "new"

class Wait(Task):
    def __init__(self, engineer: Engineer, nb_days):
        Task.__init__(self, engineer, nb_days)
    
    def toString(self):
        return "wait " + str(self.nb_of_days)
