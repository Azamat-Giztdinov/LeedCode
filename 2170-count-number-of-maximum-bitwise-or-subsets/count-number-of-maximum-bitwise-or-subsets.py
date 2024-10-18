class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        size = len(nums)
        for num in nums:
            max_or |= num

        def backTrack(index, current_or):
            if index == size:
                return int(current_or == max_or)
            return backTrack(index + 1, current_or | nums[index]) + backTrack(index + 1, current_or)
        return backTrack(0, 0)