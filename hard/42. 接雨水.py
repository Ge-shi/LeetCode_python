class Solution:
    def trap(self, height: list) -> int:
        """
        n = len(height)
        max1, max2 = 0, 0
        s1, s2 = 0, 0
        for i in range(n):
            if height[i] > max1:
                max1 = height[i]
            if height[n - i - 1] > max2:
                max2 = height[n - i - 1]
            s1 += max1
            s2 += max2
        return s1 + s2 - n * max1 - sum(height)
        """
        stacks = []
        results = 0
        for  i  in  range(len(height)):
            while  len(stacks) != 0 and height[i] >= height[stacks[-1]]:
                data = stacks.pop()
                if  len(stacks) == 0:
                    break
                results = results+(min(height[i],height[stacks[-1]])-height[data])*(i-stacks[-1]-1)
            #相等的时候不需要出来，因为比如一组数据[3,2,2,1,3],此时如果位置2上的数据2被压入栈中之后，遇到后面的3求出相应的高度min(左,右) = min(2,3) = 2,此时2-2 = 0,所以无论数据是否压入栈中都不会影响后续的结果
            stacks.append(i)
        return  results