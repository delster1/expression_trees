from treeNode import TreeNode
class ExpressionTree:
    def __init__(self, root):
        self.root = root
        self.post_order_output = ""
    def add(self, dest, entry):
        if self.root is None:
            self.root = TreeNode(entry)
            return self.root
        self.rec_add(self.root, dest, entry)


    def add_child(self, node, entry):
        if node.left is None:
            node.left = TreeNode(entry)
        elif node.right is None:
            node.right = TreeNode(entry)
        else:
            return 

    def print_post_order(self, cur_node):
        if cur_node.left:
            self.print_post_order(cur_node.left)
        if cur_node.right:
            self.print_post_order(cur_node.right)
        self.post_order_output += f"{cur_node.entry}"
        return self.post_order_output
    
    def rec_add(self, cur_node, dest, entry):
        if cur_node.entry == dest:
            self.add_child(cur_node, entry)
            return True
        elif cur_node == None:
            return False
        return self.rec_add(cur_node.left, dest, entry) or self.rec_add(cur_node.right, dest, entry)

    def print_in_order(self, cur_node):
            if cur_node.left:
                self.print_in_order(cur_node.left)  
            self.in_order_output += f"{cur_node.entry}\n"
            if cur_node.right:
                self.print_in_order(cur_node.right)
            return self.in_order_output