class MyHashSet:

    def __init__(self):
        self.keys = [[] for _ in range(10)]

    def add(self, key: int) -> None:
        bucket = key % 10
        if key not in self.keys[bucket]:
            self.keys[bucket].append(key)

    def remove(self, key: int) -> None:
        bucket = key % 10
        if key in self.keys[bucket]:
            self.keys[bucket].remove(key)

    def contains(self, key: int) -> bool:
        bucket = key % 10
        if key in self.keys[bucket]:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)