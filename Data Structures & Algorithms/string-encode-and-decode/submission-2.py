class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ""
        for s in strs:
            e += (s + chr(999))
        return e
    def decode(self, s: str) -> List[str]:
        i = 0
        d = []
        for j, c in enumerate(s):
             if c == chr(999):
                d.append(s[i:j])
                i = j+1
        return d