class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        merged_array = [0] * (n + m)
        i, j, k = 0, 0, 0
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                merged_array[k] = nums1[i]  
                i += 1
            else:
                merged_array[k] = nums2[j]
                j += 1
            k += 1
        while i < n:
            merged_array[k] = nums1[i]
            i += 1
            k += 1
        while j < m:
            merged_array[k] = nums2[j]
            j += 1
            k += 1
        return merged_array[(m + n)// 2] if (m + n) % 2 == 1 else (merged_array[(n + m) // 2] + merged_array[(n + m) // 2 - 1]) / 2