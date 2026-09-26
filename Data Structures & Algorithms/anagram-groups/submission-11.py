class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for s in strs:
            count = [0] * 26
            
            for char in s:
                i = ord(char) - ord('a')
                count[i] += 1

            count_tuple = tuple(count)

            if count_tuple in seen:
                seen[count_tuple].append(s)
            else:
                seen[count_tuple] = [s]

        return list(seen.values())