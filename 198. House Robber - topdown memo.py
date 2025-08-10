class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        memo={}

        def backtrack(index):
            if index>=n:
                return 0
            if index in memo:
                return memo[index]
            
            current = nums[index] + backtrack(index+2)
            skip = backtrack(index+1)
            memo[index] = max(current, skip)
            return memo[index]

        return backtrack(0)