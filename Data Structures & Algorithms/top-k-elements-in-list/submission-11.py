class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        counter_sorted = sorted(counter, key=counter.get, reverse=True)
        return counter_sorted[:k]