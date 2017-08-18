
class node:
    def __init__(self, value, score, prev):
        self.value = value
        self.score = score
        self.prev = prev
        self.next = []