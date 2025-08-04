class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        sm=0

        for num in nums:
            if sm<0:
                sm=0
            sm+=num
            maxsum=max(maxsum,sm)

        return maxsum