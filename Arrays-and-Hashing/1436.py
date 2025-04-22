'''
You are given the array paths, where paths[i] = [cityAi, cityBi] means
there exists a direct path going from cityAi to cityBi. Return the
destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop,
therefore, there will be exactly one destination city.
'''

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Declare a set for storing what cities exist
        city_set = set()
        # Loop through starting cities (because neither of these are answers)
        for p in paths:
            city_set.add(p[0])
        # We find the city that is not a starting one, and that is the
        # destination city
        for p in paths:
            if p[1] not in city_set:
                return p[1]
        return ""