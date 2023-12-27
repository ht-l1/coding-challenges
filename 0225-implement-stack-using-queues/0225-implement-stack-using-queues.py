class MyStack:
	# initializing the stack
    def __init__(self):
        self.q = deque()
	
	# push: append it to the right side of the queue
    def push(self, x: int) -> None:
        self.q.append(x)
	
	# take elements out
	# in a queue, you can only remove from the left
    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()
	
	# looking at the top element without taking out
    def top(self) -> int:
        return self.q[-1]
		
    def empty(self) -> bool:
        return len(self.q) == 0