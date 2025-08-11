class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=0
        curr=nums[0]-1
        for i in nums:
            if i>curr:
                nums[count] = i
                curr = i
                count+=1
        return count