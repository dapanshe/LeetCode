## use collections.OrderedDict()  otherwise TLE
class LRUCache:
    def __init__(self, capacity):
        self.dict = collections.OrderedDict()
        self.capacity = capacity
        self.len = 0

    def get(self, key):
        if key in self.dict:
            value = self.dict[key]
            del self.dict[key]
            self.dict[key] = value
            return value
        else:
            return -1

    def set(self, key, value):
        if key in self.dict:
            del self.dict[key]
            self.dict[key] = value
        else:
            if self.len == self.capacity:
                self.dict.popitem(last = False)     # last = False FIFO    last = True LIFO
                self.len -= 1
            self.dict[key] = value
            self.len += 1
