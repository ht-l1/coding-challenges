class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        
        # get the squares first, and then sort
        
        # Initialize an array to store squared values
        res = []
        
        # Loop through each element in the input array
        for n in nums:
            # square each element and append to the result array
            res.append(n*n)
            
        # sort
        res.sort()
        
        # return the sorted result
        return res