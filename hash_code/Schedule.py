from copy import deepcopy
import numpy as np

from hash_code.Task import Task, ImplementFeature, MoveService, CreateEmptyBinary, Wait
from hash_code.ObjectsStructure import Engineer, Service, Binary, Feature

class Schedule:

    def load(file_name: str):
        file = open(file_name, "r")
        print(file.read()) 

    def __init__(self, time_limit: int, engineers: list[Engineer], services: list[Service],
        binaries: list[Binary], features: list[Feature], nb_days_binary_creation: int, end_time: float = 0):
        
        self.time_limit: int = time_limit
        self.engineers: list[Engineer] = engineers
        self.services: list[Service] = services
        self.binaries: list[Binary] = binaries
        self.features: list[Feature] = features

        CreateEmptyBinary.nb_of_days = nb_days_binary_creation

        self.end_time = end_time
    
    def save(self, output_file_name: str):
        file = open(output_file_name, "w")
        file.write("Now the file has some content!")
        file.close()
    
    def copy(self):
        return deepcopy(self)

def find_solution(schedule: Schedule):
    # tri features / score = nb_points/time
    # add feature to list of features to make with optimisation
    # if work add else don't add and try next feature

    scores = np.array([feat.getDailyUsers()/feat.getDifficulty() for feat in schedule.features])
    features = np.array(schedule.features)[np.argsort(-scores)]

    def add_feat(feat: Feature) -> Schedule:
        new_schedule: Schedule = schedule.copy()

        engineer = new_schedule.engineers[0]
        binary = new_schedule.binaries[0]
        task = ImplementFeature(engineer, feat, binary)
        engineer.addTask(task)

        new_schedule.end_time += task.nb_of_days

        return new_schedule
    
    for feature in features:
        new_schedule = add_feat(feature)
        if (new_schedule.end_time < schedule.time_limit):
            schedule = new_schedule
    
    return schedule