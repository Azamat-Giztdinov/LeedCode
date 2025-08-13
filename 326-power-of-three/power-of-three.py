class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        e = log(1<<31)/log(3)//1
        N = pow(3,e)
        return n > 0 and N%n == 0 
