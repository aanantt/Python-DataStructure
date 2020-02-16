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
    def getNode(self,index):
        cur_node=self.head
        count=0
        if cur_node and count==index:
                return cur_node.value
        while cur_node:
            count+=1
            cur_node=cur_node.next
            if count==index:
                return cur_node.value
        return "Not in the list"
l=linkedList()
l.add(Node(1))
l.add(Node(2))
l.add(Node(3))
l.add(Node(4))
l.add(Node(5))
l.add(Node(6))
print(l.getNode(2))