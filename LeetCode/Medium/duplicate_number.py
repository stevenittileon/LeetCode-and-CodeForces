class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set() # makes a hashset to store the seen data
        for num in nums:
            if num in seen:
                return num # if the number is in seen, then it is the duplicate and return it
            seen.add(num)
        return -1

'''
287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and using only constant extra space.


Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3

'''