
# # def binarySearch(arr,target):
# #     left = 0
# #     right = len(arr)-1
# #     while (left<=right):
# #         mid = (left+right)//2
# #         if (arr[mid] == target):
# #             return mid
# #         elif(arr[mid] < target):
# #             left = mid+1
# #         else:
# #             right = mid-1
# #     return -1


# # arr=[1,2,3,4,5,6]

# # target = 6

# # result = binarySearch(arr, target)
# # if result != -1:
# #     print("Element is present at index %d" % result)
# # else:
# #     print("Element is not present in this array")

# class Solution:
#     def binarySearch(self, arr, target):
#         left = 0
#         right = len(arr)-1
#         while left != right:
#             mid = (left+right)//2
#             if arr[mid] == target:
#                 return mid
#             elif arr[mid] < target:
#                 left = mid+1
#             else:
#                 right = mid-1
#         return -1

# s = Solution()
# answer = s.binarySearch([1,2,3,4,5,6,7],6)
# print(answer)
# if answer != -1:
#     print("Element is present at index %d" % answer)
# else:
#     print("Element is not present in this array")

class Solution:
    def binarySearch(self, arr, target):
        left = 0
        right = len(arr)-1
        while left!=right:
            mid = (left+right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return -1

s = Solution()
answer = s.binarySearch([1,2,3,4,5],3)
if answer != -1:
    print("the target number is index %d", answer)
else:
    print("the target is not in the array")


class Solution:
    def binarySearch(self, arr, target):
        left = 0
        right = len(arr)-1
        while left != right:
            mid = (left+right)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return -1

s = Solution()
answer = s.binarySearch([1,2,3,4,5,6], 4)
if answer != -1:
    print("the number in the search is at index: %d", answer)
else:
    print("the number is not in the search index")
    

