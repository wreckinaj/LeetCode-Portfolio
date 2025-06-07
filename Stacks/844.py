'''
Given two strings s and t, return true if they are equal when both are typed
into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            # Use a stack to keep track of the characters and delete the last element
            # when we get a backspace character
            stack = []
            for c in s:
                # We simply append characters to the stack
                if c != '#':
                    stack.append(c)
                # Delete from stack only when it is not empty (otherwise runtime error)
                elif stack:
                    stack.pop()
            # Convert stack object to a string since stack arrays cannot be equal
            return "".join(stack)
        # The stack objects will need to be equal
        return build(s) == build(t)