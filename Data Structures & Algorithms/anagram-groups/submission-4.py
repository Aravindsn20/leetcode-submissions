class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #WIthout Default Dict
        # hashmap = {}
        # for s in strs:
        #     sortedS = ''.join(sorted(s))
        #     if sortedS not in hashmap:
        #         hashmap[sortedS] = []
        #     hashmap[sortedS].append(s)
        # return list(hashmap.values())\

        #With Default dict - O(n * nlogn)
        # hashmap = defaultdict(list)
        # for s in strs:
        #     sortedS = ''.join(sorted(s))
        #     hashmap[sortedS].append(s)
        # return list(hashmap.values())

        #Optimized 
        hashmap = defaultdict(list)
        for s in strs:
            arr = [0] * 26
            for ct in s:
                arr[ord(ct) - ord('a')] += 1
            hashmap[tuple(arr)].append(s)
        return list(hashmap.values())


