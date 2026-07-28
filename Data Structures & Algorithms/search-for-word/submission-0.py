class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
       

        rows = len(board)
        cols = len(board[0])

        # DFS function
        def dfs(r, c, index):

            # Entire word found
            if index == len(word):
                return True

            # Invalid conditions
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                board[r][c] != word[index]):
                return False

            # Mark current cell as visited
            temp = board[r][c]
            board[r][c] = "#"

            # Explore all 4 directions
            found = (
                dfs(r + 1, c, index + 1) or
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1)
            )

            # Backtrack
            board[r][c] = temp

            return found

        # Try every cell as the starting point
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False