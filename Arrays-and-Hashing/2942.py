'''
You are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note that the returned array may be in any order.
'''

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        # Just need to do a simple loop for this problem. If you are not using
        # Python, you will need two nested loops.
        for i in range(len(words)):
            if x in words[i]:
                ans.append(i)
        return ans