class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far=win=0
        for i in range(len(nums)-1):
            far = max(far, nums[i]+i)
            if win==i:
                if far<=win:
                    return False
                win=far
            
        return True