class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # storing all the previous elements before current
        # value : index >> mapping the value to the index of that value
        prevMap = {} 
        
        for i, n in enumerate(nums):
            diff = target - n
            # if we find the solution
            if diff in prevMap:
                return [prevMap[diff], i]
            # otherwise we do not find, continue with i
            prevMap[n] =i
        
        return