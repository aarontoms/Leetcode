class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxa=0
        n = len(matrix[0])
        def hist(heights):
            nonlocal maxa
            stack=[]
            heights.append(0)

            for i in range(n+1):
                while stack and heights[stack[-1]]>heights[i]:
                    height = heights[stack.pop()]
                    width=i if not stack else i-stack[-1]-1
                    if height*width>maxa:
                        maxa = height*width
                stack.append(i)
            
        sumrow = [0]*n
        for row in matrix:
            i=0
            while i<n:
                if row[i]=="1":
                    sumrow[i] += 1
                else:
                    sumrow[i] = 0
                i+=1
            hist(sumrow[:])
        return maxa