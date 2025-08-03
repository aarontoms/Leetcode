class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        i=0
        mn=nums[0]+nums[1]+nums[2]
        nums=sorted(nums)
        n=len(nums)

        for i in range(n-2):
            left = i+1
            right = n-1

            while left < right:
                s = nums[i]+nums[left]+nums[right]
                if abs(target-s) < abs(target-mn):
                    mn = s
                    print(mn)
                if s<target:
                    left+=1
                elif s>target:
                    right-=1
                else:
                    return s

        return mn