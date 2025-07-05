class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # input: array `nums``
        # input: interger `target``
        # output: indices of the two numbers that add up to `target`

        # hashmap {value: index} 
        seen = {}

        # n(current value), i (current index) 
        for i,n in enumerate(nums):
            diff = target - n
            if diff in seen:
                # return a pair of indices
                return [seen[diff],i]
            # if not found, store the current index, and continue loop
            # it means i saw value of n in index i
            seen[n] = i
        return