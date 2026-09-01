class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            sorted_S = "".join(sorted(s))
            hashmap[sorted_S].append(s)
        return list(hashmap.values())
        

        