class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = []
        result = []
        for s in strs:
            s_dict = {}
            for c in s:
                if c in s_dict:
                    s_dict[c] += 1
                else:
                    s_dict[c] = 1
            
            if s_dict in anagram:
                index = anagram.index(s_dict)
                result[index].append(s)
            else:
                anagram.append(s_dict)
                result.append([s])
        
        return result