class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        n = len(nums)
        nums = sorted(nums)
        res = []
        while i<n-1 and nums[i]<=0:
            left = i+1
            right = n-1
            while left<right:
                s = nums[i]+nums[left]+nums[right]
                if s==0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif s<0:
                    left+=1
                else:
                    right-=1

            while i<n-1 and nums[i]==nums[i+1]:
                i+=1
            i+=1
        return res