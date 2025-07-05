class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0 #stores current streak of 1s
        max_seen = 0 # stores the max seen

        for i in nums:
            if i == 1:
                counter += 1
                max_seen = max(counter, max_seen)
            else:
                counter = 0 #reset counter

        return max_seen
