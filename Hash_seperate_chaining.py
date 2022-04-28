class HashTables:
    def __init__(self):
        self.size = 10
        self.arr = [[] for i in range(self.size)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            # print(char,ord(char))
            hash += ord(char)
        # print(hash, hash % self.size)
        return hash % self.size

    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        # print(arr_index)
        for kv in self.arr[arr_index]:
            # print(kv[0])
            if kv[0] == key:
                # print(kv[1])
                return kv[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        # print('h = ',h)
        found = False
        for idx, element in enumerate(self.arr[h]):
            # print('idx = ',idx)
            print('element =', element)
            # print(len(element))
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
        if not found:
            self.arr[h].append((key, val))

    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("delete at ", index)
                del self.arr[arr_index][index]
