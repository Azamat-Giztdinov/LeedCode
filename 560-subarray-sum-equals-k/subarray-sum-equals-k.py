class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = defaultdict(int)
        d[0] = 1
        count = 0
        summ = 0
        for num in nums:
            summ += num
            count += d[summ - k]
            d[summ] += 1

        return count
        
        
        
        
