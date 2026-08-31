class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap = defaultdict(list)
        # for s in strs:
        #     sortedS = ''.join(sorted(s))
        #     hashmap[sortedS].append(s)
        # return list(hashmap.values())
        # Optimal Soln - 
        hashmap = defaultdict(list)
        for s in strs:
            arr = [0] * 26
            for cs in s:
                arr[ord(cs) - ord('a')] += 1
            hashmap[tuple(arr)].append(s)
        return list(hashmap.values())
