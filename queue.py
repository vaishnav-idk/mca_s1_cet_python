class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Inserted {item} into the queue.")

    def dequeue(self):
        if not self.is_empty():
            item = self.queue.pop(0)
            print(f"Removed {item} from the queue.")
            return item
        else:
            print("Queue is empty, cannot dequeue.")
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Current Queue:", self.queue)


# Example usage
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()

q.dequeue()
q.display()

q.dequeue()
q.dequeue()
q.dequeue()  # Attempt to dequeue from an empty queue
