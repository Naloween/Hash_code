
from hash_code.Task import Task, ImplementFeature, MoveService, CreateEmptyBinary, Wait
from hash_code.ObjectsStructure import Engineer, Service, Binary, Feature

class Schedule:

    def load(file_name: str):
        file = open(file_name, "r")
        print(file.read()) 

    def __init__(self, time_limit: int, engineers: list[Engineer], services: list[Service],
        binaries: list[Binary], features: list[Feature], nb_days_binary_creation: int):
        
        self.time_limit: int = time_limit
        self.engineers: list[Engineer] = engineers
        self.services: list[Service] = services
        self.binaries: list[Binary] = binaries
        self.features: list[Feature] = features

        CreateEmptyBinary.nb_of_days = nb_days_binary_creation

