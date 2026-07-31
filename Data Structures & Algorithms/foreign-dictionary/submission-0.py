class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        from typing import List


        graph = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):

            w1 = words[i]
            w2 = words[i + 1]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for j in range(min(len(w1), len(w2))):

                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break

        visit = {}
        res = []

        def dfs(ch):

            if ch in visit:
                return visit[ch]

            visit[ch] = False

            for nei in graph[ch]:

                if dfs(nei) == False:
                    return False

            visit[ch] = True
            res.append(ch)

            return True

        for ch in graph:

            if ch not in visit:
                if dfs(ch) == False:
                    return ""

        res.reverse()

        return "".join(res)