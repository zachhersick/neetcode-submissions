class MyHashMap:

    def __init__(self):
        self.pairs = [[] for _ in range(10)]
        self.size = 0
        self.capacity = 10

    def put(self, key: int, value: int) -> None:
        bucket = self.get_bucket_index(key)
        put_pair = [key, value]
        for pair in self.pairs[bucket]:
            if pair[0] == key:
                pair[1] = value
                return
        self.pairs[bucket].append(put_pair)
        self.size += 1
        if self.size / self.capacity > 0.75:
            self.resize()

    def get(self, key: int) -> int:
        bucket = self.get_bucket_index(key)
        for pair in self.pairs[bucket]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        bucket = self.get_bucket_index(key)
        for pair in self.pairs[bucket]:
            if pair[0] == key:
                self.pairs[bucket].remove(pair)
                self.size -= 1
                break
    
    def get_bucket_index(self, key: int) -> int:
        return key % self.capacity

    def resize(self) -> None:
        old_pairs = self.pairs
        self.capacity *= 2

        self.pairs = [[] for _ in range(self.capacity)]
        for bucket in old_pairs:
            for pair in bucket:
                bucket = self.get_bucket_index(pair[0])
                self.pairs[bucket].append(pair)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)