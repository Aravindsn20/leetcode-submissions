class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap = {}
        # for cs in s:
        #     hashmap[cs] = hashmap.get(cs, 0) + 1
        # for ct in t:
        #     hashmap[ct] = hashmap.get(ct, 0) - 1
        # return all(i == 0 for i in hashmap.values())

        
        # sorted_S = "".join(sorted(s))
        # sorted_T = "".join(sorted(t))

        # return sorted_S == sorted_T


        arr = [0] * 26
        for cs in s:
            arr[ord(cs) - ord('a')] += 1
        for ct in t:
            arr[ord(ct) - ord('a')] -= 1
        
        return all(i == 0 for i in arr)


