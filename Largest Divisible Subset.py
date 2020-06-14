'''
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]

'''

#code written by Rohan Kumar Roy

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
    
        n = len(nums)
        nums.sort()
        dp = [1 for i in range(n)]

        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i],dp[j]+1)

        m = max(dp)
        val = 1

        res = []
        i = 0
        while val <= m and i < n:
            if dp[i] == val:
                res.append(nums[i])
                val+=1
            i+=1

        return res