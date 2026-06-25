class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        i=0
        j=1

        while i<j and j<len(prices):
            if(prices[j]-prices[i] > max):
                max = prices[j]-prices[i]
            j+=1
            if(j>=len(prices)):
                i+=1
                j = i+1
        return max

        