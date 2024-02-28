class TreeNode:
    def __init__(self, entry):
        self.entry = entry
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.entry}"