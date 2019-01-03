class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        posMap = {}

        lenS = len(s)
        lenT = len(t)

        minWindowIndex, minWindowWidth = None, lenS + 1
        indexQueue = []

        for index in range(lenS):
            c = s[index]
            if c in t:
                prevIndex = posMap.get(c, None)
                if prevIndex != None:
                    indexQueue.remove(prevIndex)

                indexQueue.append(index)

                posMap[c] = index

                minIndex = indexQueue[0]

                if len(posMap) == lenT:
                    if index - minIndex < minWindowWidth:
                        minWindowIndex = minIndex
                        minWindowWidth = index - minIndex

        return s[minWindowIndex:minWindowIndex + minWindowWidth + 1] if minWindowIndex != None else ''




print( Solution().minWindow( "ADOBECODEBANC", "ABC" ))

