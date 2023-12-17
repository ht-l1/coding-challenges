class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # initializes two variables res and count.
        # res stores the majority element
        # count keep track of its frequency
        res, count = 0, 0

        # iterates through each element n in theinput list nums
        for n in nums:
            # Checks if the current count is zero
            if count == 0:
                res = n
            # Updates the count based on whether the current element n is equal to the potential majority element res. If they are equal, it increments the count by 1; otherwise, it decrements the count by 1.
            count += (1 if n == res else -1)
            
        return res