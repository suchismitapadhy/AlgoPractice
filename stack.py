class myStack:
    def __init__(self, stacksize):
        self.size = stacksize
        self.array = [None for i in range(self.size)]
        self.minarray = [None for i in range(self.size)]
        self.top = -1
        # top index
        self.mintop = -1

    def push(self, data):
        # if overflow don't push
        if self.top == self.size-1:
            print("Overflow, can't push")
        else:
            self.top += 1
            self.array[self.top] = data
            print("Pushed item")

            if self.mintop==-1 or data <= self.minarray[mintop]:
                self.mintop+=1
                self.minarray[mintop]=data
            else:



    def pop(self):
        # if underflow, can't pop
        if self.top == -1:
            print("Underflow, can't pop")
        else:
            item = self.array[self.top]
            self.top -= 1

            # check min array
            if item == self.minarray[mintop]:
                self.mintop-=1
            return item

    def peek(self):
        # if underflow, can't pop
        if self.top == -1:
            print("Stack empty, nothing on top")
        else:
            return self.array[self.top]

    def min(self):
        # if underflow, can't pop
        if self.mintop == -1:
            print("Stack empty, nothing on top")
        else:
            return self.minarray[self.mintop]


new_stack = myStack(5)
new_stack.push(10)
new_stack.push(7)
new_stack.push(23)
new_stack.push(9)
new_stack.push(44)
new_stack.push(44)
print(new_stack.pop())
new_stack.push(7)
print(new_stack.peek())
new_stack.push(62)
new_stack.push(4)
print(new_stack.pop())
print(new_stack.pop())
print(new_stack.pop())

