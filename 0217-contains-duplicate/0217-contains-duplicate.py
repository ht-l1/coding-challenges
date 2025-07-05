class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # input: integer array nums
        # output: true if appears more than once
        # output: false if all distinct
        # no constaints

        # use hash map, and see if any value hits 2
        seen_pair = set()

        for i in nums:
            if i in seen_pair:
                return True
            seen_pair.add(i)

        return False