
#11. container with most water
'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1

        max_water = 0
        while i < j:
            water =  min(height[i], height[j]) * (j -i)
            
            if max_water < water:
                max_water = water
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_water


