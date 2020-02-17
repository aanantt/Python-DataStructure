class Stack:
    def __init__(self):
        self.llist = []

    def pop(self):
        return self.llist.pop(0)

    def remove(self, key):
        self.llist.remove(key)

    def push(self, data):
        self.llist.insert(0, data)

    def reverse(self):
        self.llist = self.llist[::-1]
        return self.llist

    def isEmpty(self):
        return self.llist == []

    def peek(self):
        return self.llist[0]

    def size(self):
        return len(self.llist)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.size())
print(stack.isEmpty())
