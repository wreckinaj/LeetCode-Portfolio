'''
Given an array of strings strs, group the anagrams together. You can return the
answer in any order.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use a map to store strings with the same counting of each character
        ans = defaultdict(list)
        for s in strs:
            # This array is used to take s and find the count of each of the
            # 26 characters
            count = [0] * 26
            for c in s:
                # Increment the count of each character by taking each character's
                # order value
                count[ord(c) - ord("a")] += 1
            # Add the string with the specified count of characters (the strings
            # that are anagrams)
            ans[tuple(count)].append(s)
        # The values of our map are what we need to return, but we have to convert
        # them to the proper format first.
        return list(ans.values())