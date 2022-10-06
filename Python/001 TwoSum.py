class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sums = nums[i] + nums[j]
                if sums == target:
                    return [i,j]       
#edit commits
s = Solution()
answer = s.twoSum([1,2,3,4,5],9)
print(answer)

