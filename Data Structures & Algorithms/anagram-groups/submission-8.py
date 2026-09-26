class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for i, s in enumerate(strs):
            s_counter = Counter(s)
            s_tuple = tuple(sorted(s_counter.items()))
            if s_tuple in seen:
                seen[s_tuple].append(s)
            else:
                seen[s_tuple] = [s]

        return list(seen.values())