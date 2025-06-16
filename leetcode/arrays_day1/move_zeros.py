class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        current_position = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[current_position] = nums[i]
                current_position += 1
        
        for i in range(current_position, len(nums)):
            nums[i] = 0

