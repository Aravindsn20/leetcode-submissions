class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Soln - 1
        # hashmap = defaultdict(list)
        # for s in strs:
        #     sorted_s = ''.join(sorted(s))
        #     hashmap[sorted_s].append(s)
        # return list(hashmap.values())
        # soln - 1
        # for every element in the arr, convert it to its ascii equivalent array
        hashmap = defaultdict(list)
        for s in strs:
            arr = [0] * 26
            for cs in s:
                arr[ord(cs) - ord('a')] += 1
            hashmap[tuple(arr)].append(s)
        return list(hashmap.values())