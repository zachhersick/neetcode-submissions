class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] == val:
                while left <= right and nums[right] == val:
                    right -= 1
                if left >= right:
                    return count
                nums[left] = nums[right]
                count += 1
                right -= 1
            else:
                count += 1
            left += 1
        
        print(nums)
        print(count)
        
        return count