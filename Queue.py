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

while True:
    print(prompt)
    choice = input("Choose an option.")
    if choice == "1":
        print("Not implemented yet")
    elif choice == "9":
        exit()
    else:
        print("Invalid option.")