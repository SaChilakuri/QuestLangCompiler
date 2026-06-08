class Stack:
    def __init__(self):
        self.stack=[]
    
    def push(self, token):
        self.stack.append(token)
    
    def pop(self):
        return self.stack.pop()
    