class Queue:
    def __init__(self):
        self.queue = [None] * 100  # Pre-allocate a list with a fixed size
        self.front = -1
        self.rear = -1
        self.size = 100  # Maximum size of the queue

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full! Cannot add more items.")
            return
        if self.front == -1:  # Queue is empty
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = item
        print(f"{item} added to the queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot remove items.")
            return
        item = self.queue[self.front]
        print(f"{item} removed from the queue")
        self.front += 1
        # Reset front and rear if the queue becomes empty
        if self.front > self.rear:
            self.front = self.rear = -1

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue:", end=' ')
        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=' ')
        print()

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return self.rear >= self.size - 1

# Queue operations with user input
queue = Queue()
while True:
    print("\nQueue Operations:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = input("Enter item to enqueue: ")
        queue.enqueue(item)
    elif choice == 2:
        queue.dequeue()
    elif choice == 3:
        queue.display()
    elif choice == 4:
        break
    else:
        print("Invalid choice, please try again.")
