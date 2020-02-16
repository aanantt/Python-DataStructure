class Node:
    def __init__(self,value):
        self.value=value
        self.next = None
class linkedList:
    def __init__(self):
        self.head=None
    def add_at_last(self,node):
        if self.head is None:
            self.head = node
            return
        cur_node=self.head
        while cur_node.next:
            cur_node=cur_node.next
        cur_node.next=node
    def print(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.value)
            cur_node=cur_node.next

l=linkedList()
l.add_at_last(Node(1))
l.add_at_last(Node(2))
l.add_at_last(Node(3))
l.add_at_last(Node(3))
l.add_at_last(Node(2))
l.add_at_last(Node(1))
l.print()
