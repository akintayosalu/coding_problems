class Solution:
    def correctClosing(self, c, topOfStack):
        return ((topOfStack == "{" and c == "}") or 
            (topOfStack == "(" and c == ")") or 
            (topOfStack == "[" and c == "]"))

    def isValid(self, s: str) -> bool:
        stack = []
        openC = {"{", "[", "("}
        for c in s:
            if c in openC:
                stack.append(c)
            else:
                if stack and self.correctClosing(c, stack[-1]):
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
        