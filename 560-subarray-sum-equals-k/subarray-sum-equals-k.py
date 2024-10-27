class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = defaultdict(int)
        d[0] = 1
        count = 0
        runSum = 0
        for num in nums:
            runSum += num
            count += d[runSum - k]
            d[runSum] += 1
        return count
        
        
        
        
