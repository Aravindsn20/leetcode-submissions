class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # Sorted Soln - TC - O(nlogn) SC - O(1)
        # sortedS = "".join(sorted(s))
        # sortedT = "".join(sorted(t))
        # if sortedT == sortedS:
        #     return True
        # return False
        
        # Hashmap Soln TC - O(n); SC - O(N)
        # hashmap = {}
        # for cs in s:
        #     hashmap[cs] = hashmap.get(cs, 0) + 1
        # for ct in t:
        #     hashmap[ct] = hashmap.get(ct, 0) - 1
        # return all(i == 0 for i in hashmap.values())

        #Best Case - TC - O(n) SC - O(C)
        arr = [0] * 26
        for cs in s:
            arr[ord(cs) - ord('a')] += 1
        for ct in t:
            arr[ord(ct) - ord('a')] -= 1
        return all(i == 0 for i in arr)
