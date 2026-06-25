class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        answer = 0
        n = len(nums)

        for i in  range(n+1):
            answer ^= i

        for j in nums:
            answer ^= j
        
        return answer

        