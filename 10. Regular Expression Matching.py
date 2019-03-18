class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sIndex = 0
        lengthS = len( s )
        lengthP = len( p )

        if lengthP == 0:
            return lengthS == 0

        for pIndex in range( lengthP ):

            c = p[pIndex]
            if c == '*':
                s2 = sIndex
                while s2 < lengthS and ( prevChar =='.' or s[s2] == prevChar ): 
                    s2+=1                   
                    if self.isMatch( s[s2:], p[pIndex+1:]):
                        return True

            else:
                if pIndex < lengthP-1 and p[pIndex+1] == '*':
                    pass
                elif c =='.' or ( sIndex < lengthS and c == s[sIndex] ):
                    sIndex+=1               
                else:
                    return False

            prevChar = c

        if sIndex == lengthS:
            return True
        else:
            return False


print( Solution().isMatch( '', '.*'))

print( Solution().isMatch( 'a', 'ab*'))
        
print( Solution().isMatch( 'ab', '.*c'))

# print( Solution().isMatch( 'aa', 'a'))


print( Solution().isMatch( 'aa', '.*'))

print( Solution().isMatch( 'aa', 'ba.'))