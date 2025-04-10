'''
A pangram is a sentence where every letter of the English alphabet appears
at least once.

Given a string sentence containing only lowercase English letters,
return true if sentence is a pangram, or false otherwise.
'''

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # Define a set to keep track of what letters are in sentence
        char_set = set(sentence)
        # Since the set will only contain lowercase English letters,
        # and there are 26 of them, if all 26 are in the set, the
        # sentence is a pangram.
        if len(char_set) == 26:
            return True
        else:
            return False