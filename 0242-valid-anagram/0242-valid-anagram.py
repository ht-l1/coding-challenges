class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # input: strings s and t
        # output:
        #   true if t is an anagram of s
        #   false otherwise

        if sorted(s) == sorted(t):
            return True
        return False