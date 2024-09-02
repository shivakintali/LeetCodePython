from typing import List

# You are given an integer array height of length n. There are n vertical
# lines drawn such that the two endpoints of the ith line are (i, 0)
# and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that
# the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            curr_area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, curr_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
    


soln = Solution()

height = [1,8,6,2,5,4,8,3,7]
print("Input: {}".format(height))
print("Output: {}".format(soln.maxArea(height)))
assert(soln.maxArea(height) == 49)

height = [1,1]
print("Input: {}".format(height))
print("Output: {}".format(soln.maxArea(height)))
assert(soln.maxArea(height) == 1)

print("All tests passed")
