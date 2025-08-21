class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        res=[0]*(len1+len2)
        n1=n2=0

        while n1<len1 and n2<len2:
            if nums1[n1] < nums2[n2]:
                res[n1+n2] = nums1[n1]
                n1+=1
            else:
                res[n1+n2] = nums2[n2]
                n2+=1

        while n1<len1:
            res[n1+n2] = nums1[n1]
            n1+=1
        while n2<len2:
            res[n1+n2] = nums2[n2]
            n2+=1
        
        if (len1+len2)%2==0:
            return (res[(len1+len2)//2] + res[((len1+len2)//2)-1])/2
        else:
            return res[(len1+len2)//2]