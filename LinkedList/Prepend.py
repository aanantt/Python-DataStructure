class Node:
    def __init__(self,value):
        self.value=value
        self.next = None
class linkedList:
    def __init__(self):
        self.head=None
    def add_at_start(self,node):
        if self.head:
            node.next=self.head
            self.head=node
        self.head=node
    def print(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.value)
            cur_node=cur_node.next
l=linkedList()
l.add_at_start(Node(1))
l.add_at_start(Node(13))
l.add_at_start(Node(8))
l.add_at_start(Node(3))
l.add_at_start(Node(5))
l.add_at_start(Node(7))
l.print()