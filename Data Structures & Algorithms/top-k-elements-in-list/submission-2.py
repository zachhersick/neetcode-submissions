class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        most_common = counter.most_common(k)
        output = []
        for pair in most_common:
            output.append(pair[0])
        return output