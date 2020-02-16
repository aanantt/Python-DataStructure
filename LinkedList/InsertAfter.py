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
    def insertAfterNode(self,data,node):
        data=Node(data)
        if self.head:
            if self.head.value == node:
                data.next = self.head.next
                self.head.next = data
                return
            cur_node=self.head.next
            while cur_node:
                if cur_node.value==node:
                    data.next=cur_node.next
                    cur_node.next=data
                cur_node = cur_node.next
        return
l=linkedList()
l.add(Node(1))
l.add(Node(2))
l.add(Node(3))
l.add(Node(5))
l.add(Node(6))
l.add(Node(7))
l.insertAfterNode(10,2)
l.print()