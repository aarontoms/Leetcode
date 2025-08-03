class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        for param in s:

            if param=="(" or param=="[" or param=="{" or not stack:
                stack.append(param)
            elif param==")":
                if stack[-1]=="(":
                    stack.pop()
                else:
                    return False
            
            elif param=="]":
                if stack[-1]=="[":
                    stack.pop()
                else:
                    return False

            
            elif param=="}":
                if stack[-1]=="{":
                    stack.pop()
                else:
                    return False
            
        return True if not stack else False
            