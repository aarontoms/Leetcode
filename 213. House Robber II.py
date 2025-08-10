class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        memo1, memo2 = {}, {}
        def backtrack(index, end, memo):
            if index>=end:
                return 0
            if index in memo:
                return memo[index]
            
            rob = nums[index] + backtrack(index+2, end, memo)
            skip = backtrack(index+1, end, memo)
            memo[index] = max(rob, skip)
            return memo[index]

        case1 = backtrack(0, n-1, memo1)
        case2 = backtrack(1, n, memo2)
        print(case1, case2)
        return max(case1, case2)