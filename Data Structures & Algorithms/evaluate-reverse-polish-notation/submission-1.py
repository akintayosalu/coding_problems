class Solution:
    def handleOperation(self, stack, op):
        op2 = stack.pop()
        op1 = stack.pop()
        
        match op:
            case "+":
                return op1 + op2
            case "-":
                return op1 - op2
            case "*":
                return op1 * op2
            case "/":
                return op1 // op2

    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        operators = {"+", "-", "*", "/"}

        for op in tokens:
            if op in operators:
                num = self.handleOperation(numStack, op)
                numStack.append(num)
            else:
                numStack.append(int(op))
        
        return numStack[0]
        