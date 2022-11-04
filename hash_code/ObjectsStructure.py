
class Engineer:
    def __init__(self):
        self.tasks : list = []

    def getTasks(self):
        return self.tasks
    
    def addTask(self, task):
        self.tasks.append(task)

    def removeTask(self, task):
        self.tasks.remove(task)

class Binary:

    next_id: int = 0

    def __init__(self):
        self.id: int = Binary.next_id
        Binary.next_id += 1

        self.services = []
        self.engineers_working: list[(Engineer, int, int)] = []
    
    def get_nb_engineer_working(self, time: int):
        res = 0
        for (engineer, begin, end) in self.engineers_working:
            if begin <= time and time < end:
                res += 1
        return res

    def getId(self):
        return self.id
    
    def getServices(self):
        return self.services
    
    def addService(self, service):
        self.services.append(service)

    def removeService(self, service):
        self.services.remove(service)
    
    def addEngineer(self, engineer: Engineer, begin: int, end: int):
        self.engineers_working.append((engineer, begin, end))

class Service:

    def getServiceByName(name: str, services: list):
        for service in services:
            if(service.name == name):
                return service
        print("service name not found")
        return None

    def __init__(self, name: str, binary: Binary):
        self.name: str = name
        self.binary: Binary = binary

    def getBinary(self):
        return self.binary
    
    def getName(self):
        return self.name

    def setBinary(self, binary: Binary):
        self.binary = binary

class Feature:
    def __init__(self, name: str, difficulty: int, nb_daily_users: int):
        self.name: str = name
        self.services: list[Service] = []
        self.difficulty: int = difficulty
        self.nb_daily_users: int = nb_daily_users

    def getName(self):
        return self.name
    
    def getServices(self):
        return self.services
    
    def getDifficulty(self):
        return self.difficulty

    def getDailyUsers(self):
        return self.nb_daily_users
    
    def addService(self, service: Service):
        self.services.append(service)

    def removeService(self, service: Service):
        self.services.remove(service)