class Node:
    def __init__(self, element):
        self.element = element
        self.right_node = None
        self.left_node = None
class BinaryTree:
    def __init__(self,root_Node):
        self.root= root_Node
    def leftMost(self,node):  #Left Most element in a BST
        if node.left_node:
            self.leftMost(node.left_node)
            return True
        print(node.element)

tree = BinaryTree(Node(1))
tree.root.left_node = Node(2)
tree.root.right_node = Node(3)
tree.root.left_node.left_node = Node(4)
tree.root.left_node.right_node = Node(5)
tree.root.right_node.left_node = Node(6)
tree.root.right_node.right_node = Node(7)
tree.leftMost(tree.root)
