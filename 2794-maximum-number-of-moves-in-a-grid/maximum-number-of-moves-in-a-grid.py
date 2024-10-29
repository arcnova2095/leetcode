class Solution:
    def maxMoves(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        memo = {}
        def backtrack(i, j):
            # If we already calculate the moves of this grid, we return it
            if (i, j) in memo:
                return memo[(i, j)]
            max_moves = 0
            # Possible moves to the right
            for ni, nj in [(i - 1, j + 1), (i, j + 1), (i + 1, j + 1)]:
                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] > grid[i][j]:
                    max_moves = max(max_moves, 1 + backtrack(ni, nj))
            memo[(i, j)] = max_moves
            return max_moves
        result = 0
        # We start from each grid in the first column.
        for i in range(rows):
            result = max(result, backtrack(i, 0))
        return result