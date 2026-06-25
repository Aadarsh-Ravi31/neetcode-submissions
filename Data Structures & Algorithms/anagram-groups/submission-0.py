class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for i in strs:
            count = [0] * 26

            for j in i:
                count[ord(j) - ord('a')] += 1
            
            tup = tuple(count)
            if tup not in mp:
                mp[tup] = []
            
            mp[tup].append(i)

        return list(mp.values())



        