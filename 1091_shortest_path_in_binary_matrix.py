from heapq import heappop, heappush
from typing import List

# Given an n x n binary matrix grid, return the length of the shortest
# clear path in the matrix. If there is no clear path, return -1.
#
# A clear path starts at the top-left cell, ends at the bottom-right cell,
# only visits cells with value 0, and can move in any of the 8 directions.
#
# Time complexity: O(n^2 log(n))
# Space complexity: O(n^2)
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1

        def heuristic(row: int, col: int) -> int:
            return max(n - 1 - row, n - 1 - col)

        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        # Heap entries are (estimated_total_distance, distance_so_far, row, col).
        heap = [(1 + heuristic(0, 0), 1, 0, 0)]
        best_distance = {(0, 0): 1}

        while heap:
            _, distance, row, col = heappop(heap)
            if row == n - 1 and col == n - 1:
                return distance
            if distance > best_distance[(row, col)]:
                continue

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if nr < 0 or nr >= n or nc < 0 or nc >= n or grid[nr][nc] != 0:
                    continue

                next_distance = distance + 1
                if next_distance < best_distance.get((nr, nc), float("inf")):
                    best_distance[(nr, nc)] = next_distance
                    priority = next_distance + heuristic(nr, nc)
                    heappush(heap, (priority, next_distance, nr, nc))

        return -1


soln = Solution()

grid = [[0, 1], [1, 0]]
print("Input: {}".format(grid))
print("Output: {}".format(soln.shortestPathBinaryMatrix(grid)))
assert(soln.shortestPathBinaryMatrix(grid) == 2)

grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
print("Input: {}".format(grid))
print("Output: {}".format(soln.shortestPathBinaryMatrix(grid)))
assert(soln.shortestPathBinaryMatrix(grid) == 4)

grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
print("Input: {}".format(grid))
print("Output: {}".format(soln.shortestPathBinaryMatrix(grid)))
assert(soln.shortestPathBinaryMatrix(grid) == -1)

print("All tests passed")
