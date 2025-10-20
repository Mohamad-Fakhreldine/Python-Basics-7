class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue_value(self):
        node_data = input("Choose a value for the new element: ")
        new_node = Node(node_data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            print("Value successfully added.")

    def dequeue_value(self):
        if self.head is None:
            print("The queue is empty.")
        else:
            self.head = self.head.next
            print("Value successfully deleted.")

    def display_queue(self):
        current = self.head
        while current is not None:
            print(current.data, " <- ",end=" ")
            current = current.next
        return

prompt = """
1. Add an element to the end of the queue.
2. Remove the element at the front of the queue.
3. Check the first element in the queue.
4. Display the queue.
5. Check if the queue is empty.
6. Display the number of elements in the queue.
7. Reverse the queue.
8. Convert the queue into a regular python list.
9. Exit.
"""

q = Queue()

while True:
    print(prompt)
    choice = input("Choose an option: ")
    if choice == "1":
        q.enqueue_value()
    elif choice == "2":
        q.dequeue_value()
    elif choice == "3":
        q.display_queue()
    elif choice == "9":
        exit()
    else:
        print("Invalid option.")