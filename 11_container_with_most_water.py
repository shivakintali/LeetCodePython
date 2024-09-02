from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = 0
        while i < j:
            curr_area = (j - i) * min(height[i], height[j])
            max_area = max(max_area, curr_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
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
