class Solution:
    def jump(self, nums: List[int]) -> int:
        far=win=jump=0

        for i in range(len(nums)-1):
            far=max(far, nums[i]+i)
            if i==win:
                win=far
                jump+=1

        return jump