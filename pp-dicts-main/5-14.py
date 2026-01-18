from collections import deque

queue = deque()
ticket_number = 1

while True:
    print("\n1. New customer")
    print("2. Serve next")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        queue.append(ticket_number)
        print("Customer added, ticket:", ticket_number)
        ticket_number += 1

    elif choice == "2":
        if queue:
            print("Serving customer:", queue.popleft())
        else:
            print("Queue empty.")

    elif choice == "3":
        break
