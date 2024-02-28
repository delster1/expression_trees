class Node:
    def __init__(self, entry):
        self.entry = entry
        self.next = None

    def __repr__(self):
        return f"{self.entry} "
