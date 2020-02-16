class Node:
    def __init__(self, element):
        self.element = element
        self.right_node = None
        self.left_node = None
class BST:
    def __init__(self, root_Node):
        self.root= root_Node
    def rightMost(self,node):#Right Most Element in a BST
        if node.right_node:
            self.rightMost(node.right_node)
            return True
        print(node.element)

tree = BST(Node(1))
tree.root.left_node = Node(2)
tree.root.right_node = Node(3)
tree.root.left_node.left_node = Node(4)
tree.root.left_node.right_node = Node(5)
tree.root.right_node.left_node = Node(6)
tree.root.right_node.right_node = Node(7)
tree.rightMost(tree.root)