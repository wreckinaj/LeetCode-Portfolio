'''
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing
moving one unit north, south, east, or west, respectively. You start at the
origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time
you are on a location you have previously visited. Return false otherwise.
'''

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # You start at the origin
        x = 0
        y = 0
        # Use a set to keep track of what points you reach
        points = set()
        # Add the starting point
        points.add((0,0))
        for d in path:
            # Inc/decrement variables based on what direction you get
            if d == 'N':
                y += 1
            elif d == 'S':
                y -= 1
            elif d == 'E':
                x += 1
            else:
                x -= 1
            # Determine whether or not you reach a point you reached before.
            if (x,y) in points:
                return True
            # Store current point to come back to later
            else:
                points.add((x,y))
        return False