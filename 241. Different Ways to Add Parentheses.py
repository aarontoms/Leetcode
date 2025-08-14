from functools import lru_cache

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        left, right = 0, len(expression)
        res=[]
        op={
            "+": lambda x,y: x+y,
            "-": lambda x,y: x-y,
            "*": lambda x,y: x*y
        }

        @lru_cache(None)
        def dfs(left, right):
            res=[]
            for i in range(left, right+1):
                if expression[i] in op:
                    div1=dfs(left, i-1)
                    div2=dfs(i+1, right)

                    for d1 in div1:
                        for d2 in div2:
                            res.append(op[expression[i]](d1, d2))
            if res==[]:
                res.append(int(expression[left: right+1]))
            return res

        return dfs(0, right-1)