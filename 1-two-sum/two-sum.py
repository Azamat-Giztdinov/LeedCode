class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dick = {}
        size = len(nums)

        for i in range(size):
            num = target - nums[i]
            if num in nums_dick:
                return [nums_dick[num], i]
            nums_dick[nums[i]] = i
        return [] 