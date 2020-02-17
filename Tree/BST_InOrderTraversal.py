COUNT=[5]
class Node:
    def __init__(self, element):
        self.element = element
        self.right_node = None
        self.left_node = None
class BinaryTree:
    def __init__(self,root_Node):
        self.root= root_Node
    def print(self,root, space):
        if root:
            space += COUNT[0]
            self.print(root.right_node, space)
            for i in range(COUNT[0], space):
                print(end=" ")
            print(root.element)
            self.print(root.left_node, space)
    def inOrderTraversal(self,start_node,data):
        if start_node is not None:
            data=self.inOrderTraversal(start_node.left_node,data)
            data += str(start_node.element)
            data=self.inOrderTraversal(start_node.right_node,data)
        return data

tree = BinaryTree(Node(1))
tree.root.left_node = Node(2)
tree.root.right_node = Node(3)
tree.root.left_node.left_node = Node(4)
tree.root.left_node.right_node = Node(5)
tree.root.right_node.left_node = Node(6)
tree.root.right_node.right_node = Node(7)
print(tree.inOrderTraversal(tree.root,""))
