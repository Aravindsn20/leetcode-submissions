class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #loop thorufgh, pick every word
        #sort every word, and have it as a key,value in the hashmap
        hashmap = defaultdict(list)
        for s in strs:
            sorted_S = "".join(sorted(s))
            hashmap[sorted_S].append(s)
        print(hashmap.values())
        return list(hashmap.values())
            

        