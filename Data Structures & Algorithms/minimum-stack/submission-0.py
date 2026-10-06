class MinStack:

    def __init__(self):
        self.stack = []
        self.minNum = None
        
    def push(self, val: int) -> None:
        localMin = val
        if self.minNum is None or localMin < self.minNum :
            self.minNum = localMin
        self.stack.append((val, self.minNum))
        

    def pop(self) -> None:
        self.stack.pop()
        self.minNum = self.stack[-1][1]
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.minNum
        
