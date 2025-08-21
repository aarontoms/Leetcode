class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i]=0
        
        for i in range(len(nums)):
            if nums[i]<=len(nums):
                val = abs(nums[i])
                if val<1 or val>len(nums):
                    continue
                if nums[val-1]>0:
                    nums[val-1] *= -1
                elif nums[val-1]==0:
                    nums[val-1]=-(len(nums)+1)

        for i in range(1, len(nums)+1):
            if nums[i-1]>=0:
                return i
        return len(nums)+1