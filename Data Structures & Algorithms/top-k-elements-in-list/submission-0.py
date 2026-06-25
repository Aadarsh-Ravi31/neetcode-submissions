class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            freq[i] = freq.get(i,0) + 1
        
        sorted_items = sorted(freq.items(), key = lambda x : x[1], reverse = True)

        ans = []
        for j in range(k):
            ans.append(sorted_items[j][0])
        return ans
