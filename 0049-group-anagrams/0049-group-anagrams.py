class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary with default value as empty list
        res = defaultdict(list)

        for s in strs:
            # Create a count array for each of the 26 lowercase letters
            # [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
            count = [0] * 26

            # # Count frequency of each character in the string
            for c in s:
                # converts characters to indices from 0-25
                # For 'a': ord('a') - ord('a') = 97 - 97 = 0
                # For 'b': ord('b') - ord('a') = 98 - 97 = 1
                # and then increment the count of that character
                # if we see 'a', increment the count at index 0
                # if we see 'b', increment the count at index 1
                count[ord(c) - ord("a")] += 1
            
            # Convert count array to tuple so it can be used as a dictionary key
            # Append the string to its corresponding anagram group
            # eat The count array is [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
            # We convert this to a tuple and use it as a key in res
            res[tuple(count)].append(s)
        
        # Convert the dictionary values to a list and return
        return list(res.values())