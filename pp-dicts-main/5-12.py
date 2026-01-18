def reverse_string(text):
    # 1. Tworzymy pustą listę, która posłuży nam jako STOS (Stack).
    stack = []

    # 2. Operacja "PUSH" (Wkładanie na stos)
    # Przechodzimy przez każdą literę w tekście.
    for ch in text:
        # Metoda .append() dodaje element na KONIEC listy (na wierzch stosu).
        # Jeśli wpiszesz "KOT", to na dnie będzie 'K', a na wierzchu 'T'.
        stack.append(ch)

    # Przygotowujemy zmienną na wynik
    reversed_text = ""

    # 3. Operacja "POP" (Zdejmowanie ze stosu)
    # Pętla działa dopóki stos nie jest pusty (while stack).
    while stack:
        # Metoda .pop() robi dwie rzeczy:
        # a) Zwraca ostatni element listy (ten z wierzchu).
        # b) Usuwa go z listy.
        # Dzięki temu najpierw odzyskujemy literę, którą wrzuciliśmy jako ostatnią.
        reversed_text += stack.pop()

    return reversed_text

# Pobranie danych i uruchomienie funkcji
text = input("Enter text to reverse: ")
print("Reversed:", reverse_string(text))