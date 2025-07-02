class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        n = 0 
        for i in range(1,l):
            if nums[i] < nums[i - 1]:
                if not n and nums[0] >= nums[-1]:
                    n = i
                else:
                    return False                
        return True
