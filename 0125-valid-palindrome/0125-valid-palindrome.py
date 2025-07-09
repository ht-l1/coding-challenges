class Solution:
    def isPalindrome(self, s: str) -> bool:
        # input: string s
        # output: return true if palindrome, false otherwise
        
        result = ""
        for i in s:
            if i.isalnum():
                result += i.lower()
        return result == result[::-1]