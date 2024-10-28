class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = float("-INF")
        d = {}
        pre_sum = 0
        for i in nums:
            pre_sum += i

            max_num = k + i
            min_num = -k + i

            if max_num in d.keys():
                max_sum = max(max_sum, pre_sum - d[max_num] + max_num)

            if min_num in d.keys():
                max_sum = max(max_sum, pre_sum - d[min_num] + min_num)
            
            if i in d.keys():
                d[i] = min(d[i], pre_sum)
            else:
                d[i] = pre_sum
            
       
        return max_sum if max_sum != float("-INF") else 0