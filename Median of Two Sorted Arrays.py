from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        med = int( (len1+len2)/2)
        even = 1 if med*2 == len1+len2 else 0
        index1, index2 = 0, 0

        index = 0
        prev = None
        v = None
        
        for index in range( med + 1):
            if index1 >= len1:
                offset = med-index

                if offset >= even:
                    v = nums2[index2+offset]
                    if even:
                        prev = nums2[index2+offset-1]
                else:
                    prev = v
                    v = nums2[index2]
                break     

            if index2 >= len2:
                offset = med-index
                if offset >= even:
                    v = nums1[index1+offset]
                    if even:
                        prev = nums1[index1+offset-1]
                else:
                    prev = v
                    v = nums1[index1]    
                break               
                   
            prev = v

            if nums1[index1] < nums2[index2]:             
                v = nums1[index1]
                index1+=1
            else:
                v = nums2[index2]
                index2+=1

        if even:
            return (v+prev)*0.5
        else:
            return v




solution = Solution()
print( solution.findMedianSortedArrays( [1, 3], []) )
print( solution.findMedianSortedArrays( [1, 2], [3, 4]) )
print( solution.findMedianSortedArrays( [1, 3], [2]) )