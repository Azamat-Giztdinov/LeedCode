class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = 0, 0
        count_zerro1, count_zerro2 = 0, 0
        for i in nums1:
            sum1 += i
            if not i:
                count_zerro1 += 1
        sum1 += count_zerro1
        for i in nums2:
            sum2 += i
            if not i:
                count_zerro2 += 1
        sum2 += count_zerro2
        if sum1 > sum2:
            if count_zerro2:
                return sum1
            return -1
        elif sum2 > sum1:
            if count_zerro1:
                return sum2
            return -1
        return sum1
