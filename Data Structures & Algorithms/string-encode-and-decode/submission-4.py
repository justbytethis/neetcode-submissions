class Solution:
    def encode(self, strs: List[str]) -> str:
        result = "".join([f"{s}{chr(999)}" for s in strs])
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        start, end = 0, 0
        result = []
        while end < len(s):
            if s[end] == chr(999):
                result.append(s[start:end])
                start, end = end + 1, end + 1
            else:
                end += 1
        return result

            