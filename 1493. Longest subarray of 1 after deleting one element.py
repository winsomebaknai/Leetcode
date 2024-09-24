'''
1493. Longest subarrays of 1's after deleting one element
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
'''
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        maxcount = 0
        count = 0

        for j in range(len(nums)):
            if nums[j] == 0:
                count += 1
            
            while count > 1:
                if nums[i] == 0:
                    count -= 1
                i += 1
            
            maxcount = max(maxcount, j - i)
        return maxcount

        