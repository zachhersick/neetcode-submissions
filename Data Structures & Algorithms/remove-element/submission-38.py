class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        right = len(nums) - 1

        for i, num in enumerate(nums):
            if i > right:
                break
            if num == val:
                while i <= right and nums[right] == val:
                    right -= 1
                if i >= right:
                    return count
                nums[i] = nums[right]
                count += 1
                right -= 1
            else:
                count += 1
        
        return count