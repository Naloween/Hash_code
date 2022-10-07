import numpy as np

from Task import Task, ImplementFeature, MoveService, CreateEmptyBinary, Wait
from ObjectsStructure import Engineer, Service, Binary, Feature


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
        binaries: list[Binary], features: list[Feature], nb_days_binary_creation: int):
        
        self.time_limit: int = time_limit
        self.engineers: list[Engineer] = engineers
        self.services: list[Service] = services
        self.binaries: list[Binary] = binaries
        self.features: list[Feature] = features

        CreateEmptyBinary.nb_of_days = nb_days_binary_creation
    
    def fit(self):
        pass
    
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

