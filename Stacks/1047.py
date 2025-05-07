'''
You are given a string s consisting of lowercase English letters. A duplicate
removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can
be proven that the answer is unique.
'''

class Solution:
    def removeDuplicates(self, s: str) -> str:
        # Use a stack, as we always compare to the last element as we move through s
        stack = []
        for c in s:
            # If our stack is set to have two adjacent equal characters, we pop
            if stack and stack[-1]== c:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)