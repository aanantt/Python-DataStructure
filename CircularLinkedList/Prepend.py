class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        data = Node(data)
        cur_node = self.head
        data.next = self.head
        if not self.head:
            data.next = data
        else:
            while cur_node.next != self.head:
                cur_node = cur_node.next
            cur_node.next = data
        self.head = data

    def printList(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
            if cur_node == self.head:
                return
c=CircularLinkedList()
c.prepend(1)
c.prepend(2)
c.prepend(3)
c.printList()