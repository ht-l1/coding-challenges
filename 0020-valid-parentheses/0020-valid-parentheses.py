# In Python, the condition `if stack` checks if the list stack is non-empty.

class Solution:
    def isValid(self, s: str) -> bool:
        # Create a dictionary named 'Map' where each closing parenthesis is mapped to its corresponding opening parenthesis.
        # The keys of the 'Map' dictionary are )]} closing
        # The values associated with each key are ([{ opening
        Map = {")": "(", "]": "[", "}": "{"}

        # Initialize an empty stack to keep track of the opening parentheses encountered so far
        stack = []

        # Iterate over characters in the input string
        for c in s:
            # If the current character is a closing parenthesis
            if c in Map:
                # Check if the stack is not empty and the top of the stack matches the corresponding opening parenthesis
                # Map[c] retriees the values paired with
                # In Stack: Last-In, First-Out. The first to pop out is the last element. 
                if stack and stack[-1] == Map[c]:
                    # Pop the matching opening parenthesis from the stack
                    stack.pop()
                else:
                    # If the stack is empty or the top of the stack doesn't match, the parentheses are not valid
                    return False
            # If the current character is NOT a closing parenthesis (it's an opening parenthesis)
            else:
                # Push the opening parenthesis onto the stack
                stack.append(c)

        # After processing all characters in the input string
        # If the stack is not empty, return False
        if stack:
            return False

        # If the stack is empty, return True
        return True