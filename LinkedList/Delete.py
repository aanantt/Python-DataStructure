class Node:
    def __init__(self,value):
        self.value=value
        self.next = None
class linkedList:
    def __init__(self):
        self.head=None
    def add(self,node):
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
    def deleteNode(self,node):
        cur_node=self.head
        prev_node=None
        if cur_node and cur_node.value==node:
            self.head=cur_node.next
            cur_node=None
            return
        while cur_node and cur_node.value!=node:
            prev_node=cur_node
            cur_node=cur_node.next
        if cur_node is None:
            return
        prev_node.next=cur_node.next
        cur_node=None
l=linkedList()
l.add(Node(1))
l.add(Node(2))
l.add(Node(3))
l.add(Node(4))
l.add(Node(5))
l.add(Node(6))
l.deleteNode(2)
l.print()