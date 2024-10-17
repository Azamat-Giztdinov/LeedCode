class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))

        last = {int(n): i for i, n in enumerate(nums)}

        for i, digit in enumerate(nums):
            for n in range(9, int(digit), -1):
                if last.get(n, -1) > i:
                    nums[i], nums[last[n]] = nums[last[n]], nums[i]
                    return int(''.join(nums))
        return num
