'''
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and
s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or
vice-versa.
To make the string good, you can choose two adjacent characters that make the
string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique
under the given constraints.

Notice that an empty string is also good.
'''

class Solution:
    def makeGood(self, s: str) -> str:
        # My solution requires a check if the string is empty
        if not s:
            return s
        # Use a stack to keep track of the letters. We need to check the last two characters
        # each time we iterate
        stack = [s[0]]
        for i in range(1, len(s)):
            # Append the character as follows
            stack.append(s[i])
            n = len(stack)
            # We check if the lower and upper case of a letter are adjacent, but only if
            # the stack is long enough to check. We keep canceling as needed.
            while n >= 2 and (ord(stack[n - 1]) - 32 == ord(stack[n - 2]) or ord(stack[n - 1]) + 32 == ord(stack[n - 2])):
                stack.pop()
                stack.pop()
                n -= 2
        return "".join(stack)