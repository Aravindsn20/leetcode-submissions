class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap = defaultdict(list)
        # for s in strs:
        #     sorted_S = sorted(s)
        #     hashmap[tuple(sorted_S)].append(s)
        # return list(hashmap.values())


        hashmap = defaultdict(list)
        for s in strs:
            arr = [0] * 26
            for cs in s:
                arr[ord(cs) - ord('a')] += 1
            hashmap[tuple(arr)].append(s)
        return list(hashmap.values())