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
    def isPallindrome(self):
        s=""
        cur_node=self.head
        while cur_node:
            s+=str(cur_node.value)
            cur_node = cur_node.next
        return s==s[::-1]
l=linkedList()
l.add(Node(1))
l.add(Node(2))
l.add(Node(3))
l.add(Node(3))
l.add(Node(2))
l.add(Node(1))
print(l.isPallindrome())