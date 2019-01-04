from collections import Counter


class Solution:

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        posMap = {}
        freq = Counter(t)

        lenS = len(s)
        lenT = len(t)

        minWindowIndex, minWindowWidth = None, lenS + 1
        indexQueue = []

        for index in range(lenS):
            c = s[index]
            if c in t:
                indexes = posMap.get(c, None)
                if indexes != None and len(indexes) == freq[c]:
                    indexQueue.remove(indexes.pop(0))

                indexQueue.append(index)

                posMap.setdefault( c, [] ).append( index )

                minIndex = indexQueue[0]

                if len(indexQueue) == lenT:
                    if index - minIndex < minWindowWidth:
                        minWindowIndex = minIndex
                        minWindowWidth = index - minIndex

        return s[minWindowIndex:minWindowIndex + minWindowWidth + 1] if minWindowIndex != None else ''

print( Solution().minWindow( "bbaa", "aba" ))

print( Solution().minWindow( "BB", "BB" ))

print( Solution().minWindow( "ADOBECODEBANC", "ABC" ))


