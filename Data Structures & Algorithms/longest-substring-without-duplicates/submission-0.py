class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapper = {}
        i = 0
        j= 0
        count = 0

        while j < len(s):

            mapper[s[j]] = mapper.get(s[j],0)+1

            while(mapper[s[j]]>1):
                mapper[s[i]]-=1
                i+=1

            length = j - i + 1
            count = max(count,length)
            j+=1
        return count




   

        