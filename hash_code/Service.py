
from Binary import Binary

class Service:
    def __init__(self, binary: Binary):
        self.binary: Binary = binary

    def setBinary(self, binary: Binary):
        self.binary = binary
