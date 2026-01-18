stack = []

print("Enter RPN tokens (number, +, -, *, /, =):")

# Nieskończona pętla - program pyta o dane aż do momentu wpisania "="
while True:
    token = input("> ")

    # ---- 1. KONIEC OBLICZEŃ (=) ----
    if token == "=":
        # Sprawdzenie poprawności: na końcu na stosie powinien zostać tylko 1 wynik.
        if len(stack) != 1:
            print("Error: invalid expression") # Np. wpisano "2 2 =" (za mało operatorów)
        else:
            # Zdejmujemy i wyświetlamy jedyny element, który został
            print("Result:", stack.pop())
        break # Przerywamy pętlę while

    # ---- 2. OPERATORY MATEMATYCZNE ----
    elif token in ["+", "-", "*", "/"]:
        # UWAGA: Kolejność zdejmowania jest KLUCZOWA dla odejmowania i dzielenia!
        # Stos to LIFO (Last In, First Out).
        # Jeśli wpiszesz "10 2 /", to '2' jest na wierzchu, a '10' pod spodem.
        b = stack.pop() # Pobieramy liczbę z wierzchu (prawa strona działania, np. dzielnik)
        a = stack.pop() # Pobieramy liczbę spod spodu (lewa strona działania, np. dzielna)

        # Wykonujemy działanie i wrzucamy (push) WYNIK z powrotem na stos,
        # żeby mógł być użyty w kolejnych obliczeniach.
        if token == "+": stack.append(a + b)
        elif token == "-": stack.append(a - b) # Ważne: a - b, nie b - a
        elif token == "*": stack.append(a * b)
        elif token == "/": stack.append(a / b) # Ważne: a / b

    # ---- 3. LICZBY ----
    else:
        # Jeśli to nie "=" i nie operator, zakładamy, że to liczba.
        # Konwertujemy tekst na float i wrzucamy na stos.
        stack.append(float(token))