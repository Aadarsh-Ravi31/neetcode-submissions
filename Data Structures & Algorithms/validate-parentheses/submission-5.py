class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for i in s:
            if(i == '(' or i == '{' or i == '['):
                arr.append(i)
            else:
                if len(arr) < 1:
                    return False
                if(i == ')' and arr[-1] == '(') or (i == '}' and arr[-1] == '{') or (i == ']' and arr[-1] == '['):
                    arr.pop()
                else:
                    return False
        if(len(arr) == 0):
            return True
        else:
            return False

        