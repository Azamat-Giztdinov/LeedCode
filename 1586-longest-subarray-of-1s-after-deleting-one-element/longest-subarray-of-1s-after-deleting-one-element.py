class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        array = [[nums[0], 1]]
        for i in range(1, len(nums)):
            if array[-1][0] == nums[i]:
                array[-1][1] += 1
            else:
                array.append([nums[i], 1])
            
        count = 0
        for i in range(len(array)):
            if i > 0 and i < len(array) - 1 and array[i][0] == 0 and array[i][1] == 1:
                count = max(count, array[i - 1][1] + array[i + 1][1])
            elif array[i][0] == 1:
                count = max(count, array[i][1])
        return count if count < len(nums) else count - 1


