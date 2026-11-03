class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums)+1)]
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for key, value in count.items():
            freq[len(nums)-value].append(key)
        output = []
        i = 0
        while len(output) < k:
            if freq[i]:
                for num in freq[i]:
                    if len(output) < k:
                        output.append(num)
            i += 1
        return output