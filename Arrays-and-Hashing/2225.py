'''
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.
'''

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer = [[],[]]
        # Use a hash map to keep track of each player's losses
        loss_count = {}
        for match in matches:
            # Check if the winning player is in the map to ensure players without
            # losses will be accounted for in the final answer
            if match[0] not in loss_count.keys():
                loss_count[match[0]] = 0
            # Add up the losses for each player
            loss_count[match[1]] = loss_count.get(match[1], 0) + 1
        # Loop through map to determine the final answer
        for player, losses in loss_count.items():
            if losses == 0:
                answer[0].append(player)
            elif losses == 1:
                answer[1].append(player)
        # Since the results must be in increasing order, we must sort them
        answer[0].sort()
        answer[1].sort()
        return answer