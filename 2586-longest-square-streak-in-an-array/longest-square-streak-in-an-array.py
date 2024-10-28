class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        s = set(nums)
        nums.sort()
        count_max = 0
        count = 0
        for i in nums:
            num = i
            while num in s:
                count +=1
                num *= num
            count_max = max(count_max, count)
            count = 0
        return count_max if count_max > 1 else -1
