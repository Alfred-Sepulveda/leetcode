
from typing import List

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if(len(A) < 3): # check to see if length of A is greater than 3
            return False #return False if not
        i = 1 #variable i = 1

        while(i < len(A) and A[i] > A[i-1]): #i=1 len(A)=5 and A[1] > A[1-1]          
            i += 1 # add 1 to i 

        if(i == 1 or i == len(A)): #if i==1 or i==len(A) return False
            return False #returns False because it keeps increasing
        while(i < len(A) and A[i] < A[i-1]): #A[i] is decreasing
            i += 1 #add 1 to i
        return i == len(A) # returns true if i == len(A) or end of array

s = Solution()
answer = s.validMountainArray([1,1,2,3,1])
print(answer)
answer1 = s.validMountainArray([1,2,4,3,1])
print(answer1)

#length of the array is bigger than or equal to 3
#There exists some index i such that: 
# a[0]<a[1]<...<a[i]
# a[i]>a[i+1]>...>a[a.size -1]




