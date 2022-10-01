from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]):
        j = 0
        for i in nums:
            if i != 0: #were are looking a non zero elements
                nums[j] = i #nums[0] = 2 this places 2 in the index 0 if it is a non element
                j+=1 # we add 1 to j, this loop will stop at index 3
        for x in range(j, len(nums)): # range is j(3) to the length of Nums
            nums[x] = 0 
        print(nums)


s = Solution()
s.moveZeroes([0,2,0,1,4])

