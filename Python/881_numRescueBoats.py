
from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() # this will sort the list of people
        left = 0 # this will be the left pointer on the array
        right = len(people)-1 # this is the right pointer which is the end of the array
        boats_number = 0 #this is the number of boats that are needed
        while(left<=right): #while loop that executes while left <= right
            if(left == right): #if statement this will break when both are matching
                boats_number += 1 # will add 1 to the amount of boats needed
                break #will break from loop
            if(people[left]+people[right] <= limit): #will check if left and right
                # are under or equal to the limit
                left += 1 # will add 1 to left pointer if it is under the limit
            right-=1 #will decrement 1 to right pointer
            boats_number += 1 # will add 1 to boats_number
        return boats_number # returns results of boats_number

s = Solution()
answer = s.numRescueBoats([2,1,3,4],4)
print(answer)
