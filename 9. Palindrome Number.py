class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev, temp = 0, x
        while temp>0:
            digit = temp%10
            temp = temp//10
            rev = rev*10 + digit

        return True if x==rev else False