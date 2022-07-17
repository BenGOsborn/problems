class Solution:
    def findCenter(self, edges):
        visited = {}

        for fro, to in edges:
            if fro in visited:
                return fro

            if to in visited:
                return to            

            visited[to] = True
            visited[fro] = True