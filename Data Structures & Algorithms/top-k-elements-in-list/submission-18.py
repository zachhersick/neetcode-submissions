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
                if k-len(output) == 1:
                    output.append(freq[i][0])
                    break
                else:
                    for num in freq[i]:
                        output.append(num)
            i += 1
        return output