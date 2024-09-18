1679.Maximum number of k sum pairs

'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
'''

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = len(nums) -1
        count = 0


        while i < j:
            current_sum = 0
            current_sum = nums[i] + nums[j]
            if current_sum == k:
                count += 1
                i += 1
                j -= 1
            elif current_sum < k:
                i += 1
            else:
                j -= 1
        
        return count
