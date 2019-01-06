from collections import Counter
import math

class Solution:

    # def minWindow(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: str
    #     """
    #
    #     posMap = {}
    #     freq = Counter(t)
    #
    #     lenS = len(s)
    #     lenT = len(t)
    #
    #     minWindowIndex, minWindowWidth = None, lenS + 1
    #     indexQueue = []
    #
    #     for index in range(lenS):
    #         c = s[index]
    #         if c in t:
    #             indexes = posMap.get(c, None)
    #             if indexes != None and len(indexes) == freq[c]:
    #                 indexQueue.remove(indexes.pop(0))
    #
    #             indexQueue.append(index)
    #
    #             posMap.setdefault( c, [] ).append( index )
    #
    #             minIndex = indexQueue[0]
    #
    #             if len(indexQueue) == lenT:
    #                 if index - minIndex < minWindowWidth:
    #                     minWindowIndex = minIndex
    #                     minWindowWidth = index - minIndex
    #
    #     return s[minWindowIndex:minWindowIndex + minWindowWidth + 1] if minWindowIndex != None else ''

    def minWindow(self, s, t):
        filteredS = []

        lenS = len( s )

        for index in range( lenS ):
            c = s[index]
            if c in t:
                filteredS.append( ( c, index) )

        countMap = Counter( t )
        formed = 0
        counter = {}

        leftIndex, rightIndex = 0, 0
        min = ( math.inf, 0, 0 )
        while rightIndex < len( filteredS ):
            c, r = filteredS[rightIndex]
            rightIndex += 1
            counter[c] = counter.get( c, 0 )+1
            if counter[c] == countMap[c]:
                formed += 1

                if formed == len( countMap ):

                    curWidth = r - filteredS[leftIndex][1] + 1

                    if curWidth < min[0]:
                        min = (curWidth, filteredS[leftIndex][1], r)

                    # advance leftIndex
                    while leftIndex < rightIndex:
                        c, left = filteredS[leftIndex]
                        counter[c] -= 1
                        leftIndex += 1
                        if counter[c] < countMap[c]:
                            formed -= 1
                            break

                        curWidth = r - filteredS[leftIndex][1] + 1
                        if curWidth < min[0]:
                            min = (curWidth, filteredS[leftIndex][1], r)


        return s[min[1]:min[2]+1] if min[0] != math.inf else ''



print( Solution().minWindow( "bbaa", "aba" ))

print( Solution().minWindow( "BB", "BB" ))

print( Solution().minWindow( "ADOBECODEBANC", "ABC" ))


