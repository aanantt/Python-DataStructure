COUNT=[5]
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None
class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def add(self, node):
        self._add(self.root, node)

    def _add(self, cur_node, node):
        if cur_node.data < node:
            if cur_node.right_node:
                self._add(cur_node.right_node, node)
            else:
                cur_node.right_node= Node(node)
        else:
            if cur_node.left_node:
                self._add(cur_node.left_node, node)
            else:
                cur_node.left_node = Node(node)
    def print(self, root, space):
        if root:
            space += COUNT[0]
            self.print(root.right_node, space)
            for i in range(COUNT[0], space):
                print(end=" ")
            print(root.data)
            self.print(root.left_node, space)
bst=BST(10)
bst.add(8)
bst.add(9)
bst.add(15)
bst.add(4)
bst.add(13)
bst.add(16)
bst.print(bst.root,0)