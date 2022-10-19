
from copy import deepcopy
import numpy as np

from hash_code.Task import Task, ImplementFeature, MoveService, CreateEmptyBinary, Wait
from hash_code.ObjectsStructure import Engineer, Service, Binary, Feature


class Schedule:

    def load(file_name: str):
        file = open(file_name, "r")

        line = file.readline().split(" ")
        time_limit, nb_engineers, nb_services, nb_binaries, nb_features, nb_days_binary_creation = np.array(line).astype(int)

        services = [Service("none", None) for k in range(nb_services)]
        engineers = [Engineer() for k in range(nb_engineers)]
        binaries = [Binary() for k in range(nb_binaries)]
        features = [Feature("none", -1, -1) for k in range(nb_features)]

        for k in range(nb_services):
            line = file.readline().split(" ")
            services[k].name = line[0]
            services[k].binary = binaries[int(line[1])]

        for k in range(nb_features):
            line = file.readline().split(" ")
            features[k].name = line[0]
            nb_services_implemented = int(line[1])
            features[k].difficulty = int(line[2])
            features[k].nb_daily_users = int(line[3])

            line = file.readline().split(" ")
            for i in range(nb_services_implemented):
                features[k].addService(Service.getServiceByName(line[i], services))
        
        return Schedule(time_limit, engineers, services, binaries, features, nb_days_binary_creation)

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

        content = ""

        content += str(len(self.engineers))+"\n"

        for engineer in self.engineers:
            content += str(len(engineer.tasks))+"\n"
            for task in engineer.tasks:
                content += task.toString()+"\n"


        file = open(output_file_name, "w")
        file.write(content)
        file.close()
    
    def copy(self):
        return deepcopy(self)

    def getScore(self):
        score = 0
        for engineer in self.engineers:
            time = 0
            for task in engineer.tasks:
                time += task.nb_of_days
                if type(task) == type(ImplementFeature):
                    score += task.feature.getDailyUsers()*max(0, self.time_limit - time)
        return score

def find_solution(schedule: Schedule):

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