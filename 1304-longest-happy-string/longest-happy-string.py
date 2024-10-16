class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        happy_string = ''
        end_char = ''
        count = 0
        nums = [a, b, c]
        chars = ['a', 'b', 'c']
        while sum(nums) != 0:
            max_num= max(nums)
            idx = nums.index(max_num)
            if end_char != chars[idx] or count < 2:
                if end_char != chars[idx]:
                    count = 0
                happy_string += chars[idx]
                nums[idx] -= 1
                end_char = chars[idx]
                count += 1
            else:
                tmp = [i for i, num in enumerate(nums) if end_char != chars[i] and num]
                if tmp:
                    idx = tmp[0]
                    happy_string += chars[idx]
                    nums[idx] -= 1
                    count = 1
                    end_char = chars[idx]
                else:
                    break
        return happy_string