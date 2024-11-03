class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runSum = 0
        minSum = 0
        maxSum = nums[0]
        for i in nums:
            runSum += i
            maxSum = max(maxSum, runSum - minSum)
            minSum = min(minSum, runSum)
           
        return maxSum