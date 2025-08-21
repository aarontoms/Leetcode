class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)

        def backtrack(start):
            if start==n:
                res.append(nums[:])
                return
            used=set()
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                used.add(nums[i])
                nums[i], nums[start] = nums[start], nums[i]
                backtrack(start+1)
                nums[i], nums[start] = nums[start], nums[i]
        
        backtrack(0)
        return res