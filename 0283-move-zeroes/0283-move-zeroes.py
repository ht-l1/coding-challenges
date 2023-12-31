class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Two Pointer Approach
        
        slow = 0
        for fast in range(len(nums)):
            
            # swap the slow and fast
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            # increment
            if nums[slow] != 0:
                slow += 1