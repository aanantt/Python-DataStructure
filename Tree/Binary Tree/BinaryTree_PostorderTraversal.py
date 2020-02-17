COUNT=[5]
class Node:
    def __init__(self, element):
        self.element = element
        self.right_node = None
        self.left_node = None
class BinaryTree:
    def __init__(self,root_Node):
        self.root= root_Node
    def postOrderTraversal(self,start_node,data):
        if start_node is not None:
            data += str(start_node.element)
            data=self.postOrderTraversal(start_node.left_node,data)
            data=self.postOrderTraversal(start_node.right_node,data)
        return data
    def print(self,root, space):
        if root:
            space += COUNT[0]
            self.print(root.right_node, space)
            for i in range(COUNT[0], space):
                print(end=" ")
            print(root.element)
            self.print(root.left_node, space)


tree = BinaryTree(Node(1))
tree.root.left_node = Node(2)
tree.root.right_node = Node(3)
tree.root.left_node.left_node = Node(4)
tree.root.left_node.right_node = Node(5)
tree.root.right_node.left_node = Node(6)
tree.root.right_node.right_node = Node(7)
print(tree.postOrderTraversal(tree.root,""))
