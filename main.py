from stack import Stack
from expressiontree import ExpressionTree
from treeNode import TreeNode
import math
def build_tree(s):
    chars = ["(", ")", "+", "-", "*", "/", "^"]

    priority = {'(': 1,
            '+': 2,
            '-': 2,
            '*': 3,
            '/': 3,
            '^': 3
        }
    
    nodes_stack = [] # stack
    chars_stack = [] # ops

    for char in s:
        if char == "(":
            print("found open parenthesis")
            chars_stack.append(char)
        elif char not in chars:
            print("found number")
            nodes_stack.append(TreeNode(char))
        elif char == ")": # here, we will create a node for the topmost character and add existing nodes as children 
            print("found end parenthesis")
            while chars_stack[-1] != "(":
                root = TreeNode(chars_stack.pop())
                root.right = nodes_stack.pop()
                root.left = nodes_stack.pop()
                nodes_stack.append(root)
            chars_stack.pop()
        else:
            print("found operator")
            while chars_stack and priority[chars_stack[-1]] >= priority[char]:
                root = TreeNode(chars_stack.pop())
                root.right = nodes_stack.pop()
                root.left = nodes_stack.pop()
                nodes_stack.append(root)
            chars_stack.append(char)
    my_tree = ExpressionTree(nodes_stack[0])
    return my_tree.print_post_order(my_tree.root)

def compute_math(s):
    chars = ["(", ")", "+", "-", "*", "/", "^"]
    out_stack = []

    for arg in s:
        print(arg)
        print(out_stack)
        if arg in chars:
            num2 = out_stack.pop()
            num1 = out_stack.pop()
            if str(num1).strip("-1").isdigit() and str(num2).strip("-").isdigit():
                print("both digits")
                if arg == "^":
                    out_stack.append(eval(f"{num1}**{num2}"))
                else:
                    out_stack.append(eval(f"{num1}{arg}{num2}"))
            else:
                out_stack.append(f"({num1}{arg}{num2})")
        else:
            out_stack.append(arg)
    return out_stack
def main():
    s = "((5+2)^3)*(3-(5+9))-5"
    prefix = build_tree(s)
    print(prefix)
    out = compute_math(prefix)
    print(out)
main()

