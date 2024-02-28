from treeNode import TreeNode
from node import Node 
class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, entry):
        temp = Node(entry)
        temp.next = self.top
        self.top = temp

    def pop(self):
        if not self.is_empty():
            temp = self.top
            self.top = self.top.next
            return temp.entry
        raise RuntimeError('Array is Empty')

    def is_empty(self):
        if self.top == None:
            return True
        return False