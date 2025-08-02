class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = mx = 0
        right = len(height)-1
        
        while left<=right:
            h = min(height[left], height[right])
            w = right - left
            area = h*w
            mx = max(area, mx)
            
            while left<right and height[left]<=h:
                left+=1
            while left<right and height[right]<=h:
                right-=1
            
        
        return mx