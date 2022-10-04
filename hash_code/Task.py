
from Engineer import Engineer
from Feature import Feature
from Binary import Binary
from Service import Service

class Task:
    def __init__(self, engineer: Engineer, nb_of_days: int):
        self.engineer: Engineer = engineer
        self.nb_of_days: int = nb_of_days

class ImplementFeature(Task):
    def __init__(self, engineer: Engineer, feature: Feature, binary: Binary):

        nb_engineer_working_binary = 0

        Task.__init__(self, engineer, feature.difficulty + len(binary.services) + nb_engineer_working_binary)
        
        self.feature: Feature = feature
        self.binary: Binary = binary

class MoveService(Task):
    def __init__(self, engineer: Engineer, service: Service, binary: Binary):
        Task.__init__(self, engineer, max(len(service.binary.services), len(binary.services)))

        self.service: Service = service
        self.binary: Binary = binary

class CreateEmptyBinary(Task):
    def __init__(self, engineer: Engineer):
        Task.__init__(self, engineer, 0)

class Wait(Task):
    def __init__(self, engineer: Engineer):
        Task.__init__(self, engineer, 0)
