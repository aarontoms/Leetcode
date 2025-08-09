class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minprod=maxprod=prod=nums[0]

        for num in nums[1:]:
            temp=maxprod
            maxprod = max(num, num*temp, num*minprod)
            minprod = min(num, num*temp, num*minprod)
            prod = max(prod, maxprod)
        return prod