class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for string in strs:
            str_sorted = "".join(sorted(string))
            if str_sorted in result:
                result[str_sorted].append(string)
            else:
                result[str_sorted] = [string]
        
        return [v for k, v in result.items()]