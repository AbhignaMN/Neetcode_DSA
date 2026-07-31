class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from typing import List



        graph = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            graph[course].append(pre)

        visit = set()
        cycle = set()

        def dfs(course):

            if course in cycle:
                return False

            if course in visit:
                return True

            cycle.add(course)

            for pre in graph[course]:
                if not dfs(pre):
                    return False

            cycle.remove(course)
            visit.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True