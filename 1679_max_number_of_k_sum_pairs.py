from typing import List

# You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose
# sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.

# Time complexity: O(n log(n))
# Space complexity: O(log(n))
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r, ans = 0, len(nums) - 1, 0
        while l < r:
            s = nums[l] + nums[r]
            if s == k:
                ans += 1
                l, r = l + 1, r - 1
            elif s > k:
                r -= 1
            else:
                l += 1
        return ans


soln = Solution()

nums, k = [1,2,3,4], 5
print("Input: nums = {} k = {}".format(nums, k))
print("Output: {}".format(soln.maxOperations(nums, k)))

nums, k = [3,1,3,4,3], 6
print("Input: nums = {} k = {}".format(nums, k))
print("Output: {}".format(soln.maxOperations(nums, k)))


print("Done")
