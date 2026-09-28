class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        high = None
        count = 0

        for num in nums:
            if high is None:
                high = num
                count = 1
            elif num != high:
                count -= 1
                if count == 0:
                    high = num
                    count = 1
            else:
                count += 1
              
        return high