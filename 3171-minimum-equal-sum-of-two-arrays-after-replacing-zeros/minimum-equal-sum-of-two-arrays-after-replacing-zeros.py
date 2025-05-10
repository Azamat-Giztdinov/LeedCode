class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        count_zerro1, count_zerro2 = nums1.count(0), nums2.count(0)
        sum1 = sum(nums1) + count_zerro1
        sum2 = sum(nums2) + count_zerro2

        if (sum1 > sum2 and not count_zerro2) or (sum2 > sum1 and not count_zerro1):
            return -1
        return max(sum1, sum2)
