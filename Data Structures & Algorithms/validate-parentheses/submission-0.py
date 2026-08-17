class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        tos = 0
        dict_brac = {")": "(", "]": "[", "}": "{"}
        s = [ch for ch in s]
        for ele in s:
            if ele in dict_brac:
                if stack and stack[-1] == dict_brac[ele]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ele)
        
        if len(stack) == 0:
            return True
        return False