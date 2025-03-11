class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min = nums[0]
        for num in nums: 
            if abs(min) > abs(num):
                min = num
            if abs(min) == abs(num):
                min = max(min, num)
        return min

        # Space Complexity: O(1)
        # Time Complexity: O(n)

