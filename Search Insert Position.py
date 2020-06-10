'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0

'''

#code written by Rohan Kumar Roy

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums.count(target)>0:
            return nums.index(target)
        else:
            i=0
            while(i<len(nums) and target>nums[i]):
                i+=1
            return i              