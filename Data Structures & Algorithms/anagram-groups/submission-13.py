class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Approach 1 - Sort the wod and add it to teh hashmap
        # hashmap = defaultdict(list)
        # for s in strs:
        #     sorted_S = "".join(sorted(s))
        #     hashmap[sorted_S].append(s)
        # return list(hashmap.values())
        # Approach 2 - Sort the words and Add it to the constant arr size. 
        hashmap = defaultdict(list)
        for s in strs:
            arr = [0] * 26
            for cs in s:
                arr[ord(cs) - ord('a')] += 1
            hashmap[tuple(arr)].append(s)
        return list(hashmap.values())
        