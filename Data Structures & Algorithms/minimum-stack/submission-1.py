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
        if self.stack:
            self.minNum = self.stack[-1][1]
        else:
            self.minNum = None
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.minNum
        
