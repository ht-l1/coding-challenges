class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(input_str):
            stack = []
            for char in input_str:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return stack
        
        processed_s = process_string(s)
        processed_t = process_string(t)
        
        return processed_s == processed_t