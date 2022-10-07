
from Service import Service

class Feature:
    def __init__(self, difficulty: int, nb_daily_users: int):
        self.services: list[Service] = []
        self.difficulty: int = difficulty
        self.nb_daily_users: int = nb_daily_users
    
    def addService(self, service: Service):
        self.services.append(service)

    def removeService(self, service: Service):
        self.services.remove(service)
