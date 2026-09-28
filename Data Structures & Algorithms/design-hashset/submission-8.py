class MyHashSet:

    def __init__(self):
        self.keys = [[] for _ in range(10)]
        self.size = 0
        self.capacity = 10

    def add(self, key: int) -> None:
        bucket = self.get_bucket_index(key)
        if key not in self.keys[bucket]:
            self.keys[bucket].append(key)
            self.size += 1
        if self.size / self.capacity >= 0.75:
            self.resize()

    def remove(self, key: int) -> None:
        bucket = self.get_bucket_index(key)
        if key in self.keys[bucket]:
            self.keys[bucket].remove(key)
            self.size -= 1

    def contains(self, key: int) -> bool:
        bucket = self.get_bucket_index(key)
        return key in self.keys[bucket]

    def get_bucket_index(self, key: int) -> int:
        return key % self.capacity

    def resize(self):
        old_keys = self.keys

        self.capacity *= 2
        self.keys = [[] for _ in range(self.capacity)]

        for bucket in old_keys:
            for key in bucket:
                new_bucket = key % self.capacity
                self.keys[new_bucket].append(key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)