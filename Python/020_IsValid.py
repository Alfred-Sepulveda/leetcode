from fileinput import close
from re import S


class Solution:
    def isValid(self, s:str) -> bool:
        closedToOpen = {")":"(","]":"[","}":"{"}
        stack = []
        for i in s:
            if i in closedToOpen:
                if stack and stack[-1] == closedToOpen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False

#mistakes I made were if i in closedToOpen loop. it has to be i not s. Also stack and 
#stack[-1] == closedToOpen[i] in order to stack.pop() or remove the bracket from the
#stack
s = Solution()
answer = s.isValid('[({{}})]')
print(answer)
