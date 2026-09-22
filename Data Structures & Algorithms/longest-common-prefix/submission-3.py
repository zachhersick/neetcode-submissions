class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        i = 0

        while i < len(min(strs, key=len)):
            char = strs[0][i]
            for s in strs:
                if s[i] != char:
                    return output
            output += char
            i += 1
        
        return output