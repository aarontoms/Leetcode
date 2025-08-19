from functools import lru_cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]

        @lru_cache(None)
        def backtrack(left, right):
            if left+1==right:
                return 0

            res = 0
            for i in range(left+1,right):
                res = max(res, (nums[left]*nums[i]*nums[right]) + backtrack(left, i) + backtrack(i, right))
            return res

        return backtrack(0, len(nums)-1)