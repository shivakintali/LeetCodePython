from typing import List

# There are n kids with candies. You are given an integer array candies,
# where each candies[i] represents the number of candies the ith kid has,
# and an integer extraCandies, denoting the number of extra candies that
# you have.

# Return a boolean array result of length n, where result[i] is true if,
# after giving the ith kid all the extraCandies, they will have the 
# greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        return [candy + extraCandies >= mx for candy in candies]
    

soln = Solution()

candies = [2,3,5,1,3]
extraCandies = 3
print("Input: {} {}".format(candies, extraCandies))
print("Output: {}".format(soln.kidsWithCandies(candies, extraCandies)))

candies = [4,2,1,1,2]
extraCandies = 1
print("Input: {} {}".format(candies, extraCandies))
print("Output: {}".format(soln.kidsWithCandies(candies, extraCandies)))

candies = [12,1,12]
extraCandies = 10
print("Input: {} {}".format(candies, extraCandies))
print("Output: {}".format(soln.kidsWithCandies(candies, extraCandies)))


print("Done")
