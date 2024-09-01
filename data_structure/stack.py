class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} onto the stack.")

    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"Popped {item} from the stack.")
            return item
        else:
            print("Stack is empty, cannot pop.")
            return None

    def peek(self):
        if not self.is_empty():
            print(f"Top of the stack is {self.stack[-1]}")
            return self.stack[-1]
        else:
            print("Stack is empty.")
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Current Stack:", self.stack)


# Example usage
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.display()

s.pop()
s.display()

s.peek()
s.pop()
s.pop()
s.pop()  # Attempt to pop from an empty stack
