'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create a map to count how many of each letter in magazine, which
        # states how many of each letter we are allowed to use
        mag_map = {}
        for c in magazine:
            mag_map[c] = mag_map.get(c,0) + 1
        for c in ransomNote:
            # If a letter is not in magazine, or we used more than allowed,
            # we cannot create ransomNote
            if c not in mag_map.keys() or mag_map[c] == 0:
                return False
            else:
                mag_map[c] -= 1
        return True