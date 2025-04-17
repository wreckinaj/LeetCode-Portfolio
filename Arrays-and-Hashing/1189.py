'''
Given a string text, you want to use the characters of text to form as
many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum
number of instances that can be formed.
'''

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        num_map = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n':0}
        for c in text:
            if c in num_map:
                if(c == 'l' or c == 'o'):
                    num_map[c] += 0.5
                else:
                    num_map[c] += 1
        min = float('inf')
        for c in num_map:
            if num_map[c] < min:
                min = floor(num_map[c])
        return min