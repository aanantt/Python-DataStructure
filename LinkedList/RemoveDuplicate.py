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
    def removeDuplicate(self):
        cur_node=self.head
        prev_node=None
        duplicate={}
        if cur_node:
            while cur_node:
                if cur_node.value in duplicate:
                    prev_node.next = cur_node.next
                    cur_node = None
                else:
                    duplicate[cur_node.value] = 1
                    prev_node = cur_node
                cur_node = prev_node.next
        return
    def print(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.value)
            cur_node=cur_node.next
l=linkedList()
l.add(Node(1))
l.add(Node(2))
l.add(Node(3))
l.add(Node(3))
l.add(Node(2))
l.add(Node(1))
l.removeDuplicate()
l.print()
