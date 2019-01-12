# https://www.leetfree.com/problems/android-unlock-patterns.html
class Solution:

    invalids = { (1, 2, 3), (1, 4, 7), (1, 5, 9), (2, 5, 8), (3, 5, 7), (3, 6, 9), (4, 5, 6), (7, 8, 9), }


    def selectOne(self, keys, minKeyCount, maxKeyCount, lastKey = 0 ):

        count = 0
        keyCount = len( keys )
        selectedKeyCount = 9-keyCount
        if selectedKeyCount < maxKeyCount:
            for i in range( keyCount ):
                nextKey = keys[ i ]
                # check if invalid
                valid = True
                for invalid in self.invalids:
                    if ( invalid[0] == lastKey and invalid[2] == nextKey and invalid[1] in keys ) or\
                        (invalid[2] == lastKey and invalid[1] == nextKey and invalid[1] in keys):
                        valid = False
                        break

                if valid:
                    newKeys = list(keys)
                    del newKeys[i]
                    subCount = self.selectOne(newKeys, minKeyCount, maxKeyCount, nextKey )
                    if selectedKeyCount + 1 >= minKeyCount:
                        count += subCount + 1

        return count




    def getCount( self, m, n ):


        keys = [ i for i in range( 1, 10 ) ]


        count = self.selectOne( keys, m, n )
        return count


print( Solution().getCount( 1, 1) )
print( Solution().getCount( 1, 3) )


