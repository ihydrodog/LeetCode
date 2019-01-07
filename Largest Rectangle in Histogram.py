class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        heightStack = []
        largestArea = 0
        lastHeight = 0
        heights.append( 0 )
        for index, h in enumerate( heights ):

            # find largest
            x = index
            if lastHeight > h:
                valid = []
                for x0, h0 in heightStack:
                    if h0 >= h:
                        x = min( x, x0 )

                        if h0 > h:
                            largestArea = max( largestArea, (index-x0)*h0 )
                    else:
                        valid.append( (x0, h0 ))

                heightStack = valid
            heightStack.append((x, h))
            lastHeight = h


        return largestArea

l = [2,1,5,6,2,3]

print( Solution().largestRectangleArea( l ) )

