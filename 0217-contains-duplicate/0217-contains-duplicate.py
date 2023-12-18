  # use HashSet to keep track of unique elements while iterating

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    
    # HashSet Initialization creates an empty set named 'hashset'. This set will be used to keep track of unique elements encountered in the array.
    # set() is a data type representing an unordered collection of unique elements
        hashset = set()
    
        # Iterating Through the Array:
        for n in nums:
            
            # Checking for Duplicates:
            if n in hashset:
                return True
            
            # Adding to HashSet:
            hashset.add(n)
        return False
