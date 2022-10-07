
from Task import Task

class Engineer:
    def __init__(self):
        self.task: Task = None
    
    def setTask(self, task: Task):
        self.task = task
