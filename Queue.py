class Queue:
    def __init__(self):
        self.llist = []

    def push(self, key):
        self.llist.insert(0, key)

    def pop(self):
        return self.llist.pop()

    def isEmpty(self):
        return self.llist[0]

    def reverse(self):
        self.llist = self.llist[::-1]
        return self.llist

    def size(self):
        return len(self.llist)


queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.isEmpty())
