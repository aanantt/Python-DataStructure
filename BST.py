COUNT=[5]
class Node:
    def __init__(self, element):
        self.element = element
        self.right_node = None
        self.left_node = None
class BST:
    def __init__(self,root_Node):
        self.root= root_Node
    def postOrderTraversal(self,start_node,data):
        if start_node is not None:
            data += str(start_node.element)
            data=self.postOrderTraversal(start_node.left_node,data)
            data=self.postOrderTraversal(start_node.right_node,data)
        return data
    def preOrderTraversal(self,start_node,data):
        if start_node:
            data = self.postOrderTraversal(start_node.left_node, data)
            data = self.postOrderTraversal(start_node.right_node, data)
            data += str(start_node.element)
        return data

    def inOrderTraversal(self,start_node,data):
        if start_node is not None:
            data=self.postOrderTraversal(start_node.left_node,data)
            data += str(start_node.element)
            data=self.postOrderTraversal(start_node.right_node,data)
        return data
    def rightMost(self,node):   #Right Most Element in a BST
        if node.right_node:
            self.rightMost(node.right_node)
            return True
        print(node.element)
    def leftMost(self,node):  #Left Most element in a BST
        if node.left_node:
            self.leftMost(node.left_node)
            return True
        print(node.element)

    def print(self,root, space):
        if root:
            space += COUNT[0]
            self.print(root.right_node, space)
            for i in range(COUNT[0], space):
                print(end=" ")
            print(root.element)
            self.print(root.left_node, space)


tree = BST(Node(1))
tree.root.left_node = Node(2)
tree.root.right_node = Node(3)
tree.root.left_node.left_node = Node(4)
tree.root.left_node.right_node = Node(5)
tree.root.right_node.left_node = Node(6)
tree.root.right_node.right_node = Node(7)
# print(tree.postOrderTraversal(tree.root,""))
# print(tree.inOrderTraversal(tree.root,""))
# print(tree.postOrderTraversal(tree.root,""))
# tree.rightMost(tree.root)
# tree.leftMost(tree.root)
tree.print(tree.root,0)