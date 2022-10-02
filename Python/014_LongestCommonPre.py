from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        return result

#longest common prefix uses [flower, flow, flight] and takes the prefix of the common
#letters used. we used range(len(strs[0])) then followed by s in strs which will give
#us the next word used. it searches i equals len(s) followed by an or statement s[i]
#with not in with the letters of the previous word strs[0][i]. It will then return the
#results, once the for loop is finished, strs[0][i] gets added to the result. Once that
#loop is finished it returns the result.
s = Solution()
answer = s.longestCommonPrefix(['flower','flow','flight'])
print(answer)


