from collections import deque

# ---- 1. PRZYGOTOWANIE STRUKTUR ----
# deque (double-ended queue) to ulepszona lista, zoptymalizowana do szybkiego
# dodawania i usuwania elementów z obu stron.
# Idealna do tworzenia prawdziwych kolejek.
queue = deque()

# Licznik numerków (zaczynamy od klienta nr 1)
ticket_number = 1

while True:
    print("\n1. New customer")
    print("2. Serve next")
    print("3. Exit")

    choice = input("Choice: ")

    # ---- 2. NOWY KLIENT (WCHODZI DO KOLEJKI) ----
    if choice == "1":
        # .append() dodaje element na KONIEC kolejki.
        # Klient bierze numerek i staje na końcu ogonka.
        queue.append(ticket_number)
        print("Customer added, ticket:", ticket_number)
        
        # Zwiększamy licznik, żeby następny klient dostał wyższy numer.
        ticket_number += 1

    # ---- 3. OBSŁUGA KLIENTA (WYCHODZI Z KOLEJKI) ----
    elif choice == "2":
        if queue:
            # .popleft() to KLUCZOWA różnica względem stosu!
            # Usuwamy i pobieramy element z LEWEJ strony (z początku).
            # Obsługujemy tego, kto czekał najdłużej (FIFO).
            # Gdybyś użył zwykłego .pop(), obsłużyłbyś tego, co dopiero przyszedł (LIFO).
            print("Serving customer:", queue.popleft())
        else:
            print("Queue empty.") # Nie ma kogo obsługiwać

    elif choice == "3":
        break