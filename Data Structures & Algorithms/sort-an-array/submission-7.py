class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length == 0 or length == 1:
            return nums
        else:
            mid = length // 2 - 1
            first = self.sortArray(nums[:mid+1])
            second = self.sortArray(nums[mid+1:])
            left = 0
            right = 0
            comb = []
            while left < len(first) or right < len(second):
                if left == len(first):
                    comb.append(second[right])
                    right += 1
                elif right == len(second) or first[left] <= second[right]:
                    comb.append(first[left])
                    left += 1
                else:
                    comb.append(second[right])
                    right += 1
            return comb