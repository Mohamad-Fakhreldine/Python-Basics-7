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

    def check_first(self):
        if self.head is None:
            print("The queue is empty.")
        else:
            print("The next element in the queue is: ", self.head)

    def is_empty(self):
        if self.head is None:
            print("The queue is empty.")
        else:
            print("The queue is not empty.")

    def total_elements(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        print("The total number of elements in the queue is: ", count)

    #   def reverse_queue(self):
    #       #Time Complexity: O(n^2)
    #       current = self.head
    #       while current.next is not None:
    #           current = current.next
    #       self.tail = self.head
    #       self.head = current
    #       temp = self.tail
    #       while current != temp:
    #           while temp.next is not current and current is not self.tail:
    #               temp = temp.next
    #           current.next = temp
    #           current = current.next
    #           self.tail.next = None
        
    #Time Complexity: O(n)
    def reverse_queue(self):
        prev = None
        current = self.head
        self.tail = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def convert_list(self):
        new_list = []
        current = self.head
        while current is not None:
            new_list.append(int(current.data))
            current = current.next
        print("The new list is: ", new_list)
    
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
        q.check_first()
    elif choice == "4":
        q.display_queue()
    elif choice == "5":
        q.is_empty()
    elif choice == "6":
        q.total_elements()
    elif choice == "7":
        q.reverse_queue()
    elif choice == "8":
        q.convert_list()
    elif choice == "9":
        exit()
    else:
        print("Invalid option.")