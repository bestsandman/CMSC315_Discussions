"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # A standard Python list serves as the underlying dynamic array.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Appending to the end of the list places elements on top of the stack,
        # ensuring the most recently added element is accessed first (LIFO).
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # If the stack is empty, return None to prevent an IndexError crash.
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Peek inspects the top/last element without modifying the stack contents.
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # collections.deque provides O(1) time complexity for additions and removals.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Appending to the right end preserves the arrival sequence needed for FIFO behavior.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # If the queue is empty, return None to safely handle underflow without crashing.
        if self.is_empty():
            return None
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Front inspects the oldest remaining element in the queue without removing it.
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    print("\n=== STACK DEMO ===")
    demo_stack = Stack()

    # 1 & 2. Push at least 4 values (simulating a text editor undo history)
    actions = ["Type 'Hello'", "Format Bold", "Insert Image", "Change Color"]
    for action in actions:
        print(f"Pushing action onto stack: {action}")
        demo_stack.push(action)

    # 3. View top element
    print(f"Top element on stack (peek): {demo_stack.peek()}")

    # 4. Demonstrate LIFO behavior
    print("\nPopping actions from stack (demonstrating LIFO):")
    while not demo_stack.is_empty():
        print(f"Undoing / Popping: {demo_stack.pop()}")

    # 5. Popping from empty stack
    print("\nEdge Case: Popping from empty stack:")
    print(f"Result: {demo_stack.pop()}")

    # 6. Peeking at empty stack
    print("\nEdge Case: Peeking at empty stack:")
    print(f"Result: {demo_stack.peek()}")

    # 7. Single-item stack test
    print("\nEdge Case: Single-item stack test:")
    single_stack = Stack()
    single_stack.push("Only Item")
    print(f"Pushed: {single_stack.peek()}")
    print(f"Popped: {single_stack.pop()}")
    print(f"Is single-item stack empty after pop? -> {single_stack.is_empty()}")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    print("\n=== QUEUE DEMO ===")
    demo_queue = Queue()

    # 1 & 2. Enqueue at least 4 values (simulating a printer spooler)
    print_jobs = ["Report.pdf", "Invoice.docx", "Slides.pptx", "Summary.txt"]
    for job in print_jobs:
        print(f"Enqueuing print job: {job}")
        demo_queue.enqueue(job)

    # 3. View front element
    print(f"Job at the front of queue (front): {demo_queue.front()}")

    # 4. Demonstrate FIFO behavior
    print("\nProcessing jobs from queue (demonstrating FIFO):")
    while not demo_queue.is_empty():
        print(f"Printing / Dequeuing: {demo_queue.dequeue()}")

    # 5. Dequeuing from empty queue
    print("\nEdge Case: Dequeuing from empty queue:")
    print(f"Result: {demo_queue.dequeue()}")

    # 6. Viewing front of empty queue
    print("\nEdge Case: Viewing front of empty queue:")
    print(f"Result: {demo_queue.front()}")

    # 7. Single-item queue test
    print("\nEdge Case: Single-item queue test:")
    single_queue = Queue()
    single_queue.enqueue("Single Print Job")
    print(f"Enqueued: {single_queue.front()}")
    print(f"Dequeued: {single_queue.dequeue()}")
    print(f"Is single-item queue empty after dequeue? -> {single_queue.is_empty()}")


if __name__ == "__main__":
    main()