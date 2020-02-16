class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        data = Node(data)
        if not self.head:
            self.head = data
            self.head.next = self.head
            return
        cur_node = self.head
        while cur_node.next != self.head:
            cur_node = cur_node.next
        cur_node.next = data
        data.next = self.head

    def printList(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
            if cur_node == self.head:
                return
    def deleteByValue(self, key):
        if self.head.data == key:
            cur_node = self.head
            while cur_node != self.head:
                cur_node = cur_node.next
            cur_node.next = self.head.next
            self.head = self.head.next
        else:
            cur_node = self.head
            prev_node = None
            while cur_node.next != self.head:
                prev_node = cur_node
                cur_node = cur_node.next
                if cur_node.data == key:
                    prev_node.next = cur_node.next
                    cur_node = cur_node.next
c=CircularLinkedList()
c.append(1)
c.append(2)
c.append(3)
c.append(4)
c.printList()
c.deleteByValue(3)
print("After Deletion")
c.printList()