'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and 
']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        # Use a deque to reduce time complexity
        stack = deque()
        for c in s:
            # Append to stack when we get a new opening brace
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            # Cannot pop from an empty stack
            elif len(stack) == 0:
                return False
            # Check if we are popping elements from the stack in LIFO
            elif c == ')':
                if stack.pop() != '(':
                    return False
            elif c == '}':
                if stack.pop() != '{':
                    return False
            elif c == ']':
                if stack.pop() != '[':
                    return False
        # Stack must be empty
        return len(stack) == 0