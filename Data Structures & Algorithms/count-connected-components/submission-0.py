class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from typing import List



        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visit = set()

        def dfs(node):

            if node in visit:
                return

            visit.add(node)

            for nei in graph[node]:
                dfs(nei)

        count = 0

        for node in range(n):

            if node not in visit:
                count += 1
                dfs(node)

        return count