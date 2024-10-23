class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        for s in strs:
            key = ''.join(sorted(s))
            if not key in str_dict.keys():
                str_dict[key] = [s]
            else:
                str_dict[key].append(s)
        return [str_dict[i] for i in str_dict.keys()]