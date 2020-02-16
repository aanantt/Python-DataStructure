class HashMap:
    def __init__(self):
        self.size = 5
        self.hashtable = [None] * self.size

    def get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self.get_hash(key)
        key_value = [key, value]

        if self.hashtable[key_hash] is None:
            self.hashtable[key_hash] = list([key_value])
            return True
        else:
            for pair in self.hashtable[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.hashtable[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.get_hash(key)
        if self.hashtable[key_hash] is not None:
            for pair in self.hashtable[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.get_hash(key)

        if self.hashtable[key_hash] is None:
            return False
        for i in range(0, len(self.hashtable[key_hash])):
            if self.hashtable[key_hash][i][0] == key:
                self.hashtable[key_hash].pop(i)
                return True
        return False

    def keys(self):
        arr = []
        for i in range(0, len(self.hashtable)):
            if self.hashtable[i]:
                arr.append(self.hashtable[i][0])
        return arr

    def print(self):
        for item in self.hashtable:
            if item is not None:
                print(str(item))


h = HashMap()
h.add('India', '4394')
h.add('USA', '4388')
h.add('Canada', '8563')
h.add('China', '1267')
h.add('Turkey', '9574')
h.add('Mexico', '4314')
h.add('Italy', '1234')
h.print()
h.delete('China')
h.print()