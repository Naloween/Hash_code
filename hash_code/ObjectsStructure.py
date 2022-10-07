
class Engineer:
    def __init__(self):
        self.task = None
    
    def setTask(self, task):
        self.task = task

class Binary:

    next_id: int = 0

    def __init__(self):
        self.id: int = Binary.next_id
        Binary.next_id += 1

        self.services = []
        self.engineers_working: list[Engineer] = []
    
    def addService(self, service):
        self.services.append(service)

    def removeService(self, service):
        self.services.remove(service)
    
    def addEngineer(self, engineer: Engineer):
        self.engineers_working.append(engineer)

    def removeEngineer(self, engineer: Engineer):
        self.engineers_working.remove(engineer)

class Service:
    def __init__(self, name: str, binary: Binary):
        self.name: str = name
        self.binary: Binary = binary

    def setBinary(self, binary: Binary):
        self.binary = binary

class Feature:
    def __init__(self, name: str, difficulty: int, nb_daily_users: int):
        self.name: str = name
        self.services: list[Service] = []
        self.difficulty: int = difficulty
        self.nb_daily_users: int = nb_daily_users
    
    def addService(self, service: Service):
        self.services.append(service)

    def removeService(self, service: Service):
        self.services.remove(service)