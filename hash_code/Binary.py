
from Service import Service
from Engineer import Engineer

class Binary:

    next_id: int = 0

    def __init__(self):
        self.id: int = Binary.next_id
        Binary.next_id += 1

        self.services: list[Service] = []
        self.engineers_working: list[Engineer] = []
    
    def addService(self, service: Service):
        self.services.append(service)

    def removeService(self, service: Service):
        self.services.remove(service)
    
    def addEngineer(self, engineer: Engineer):
        self.engineers_working.append(engineer)

    def removeEngineer(self, engineer: Engineer):
        self.engineers_working.remove(engineer)
