class Solution:
    def isPalindrome(self, s: str) -> bool:
        # input: string s
        # output: return true if palindrome, false otherwise
        
        result = []
        for i in s:
            if i.isalnum():
                result.append(i.lower())

        # if reads the same forward and backward
        cleaned = "".join(result)
        if cleaned[0::] == cleaned[::-1]:
            return True
        return False