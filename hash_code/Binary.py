
from Service import Service

class Binary:

    next_id: int = 0

    def __init__(self):
        self.id: int = Binary.next_id
        Binary.next_id += 1

        self.services: list[Service] = []
