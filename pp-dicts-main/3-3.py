import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
    # 1. Tworzymy stos. Będziemy tu odkładać otwarte nawiasy, które "czekają" na zamknięcie.
    stack = queue.LifoQueue()
    
    # 2. Mapa par: Klucz to nawias zamykający, wartość to wymagany otwierający.
    # Dzięki temu łatwo sprawdzić, czy ')' pasuje do '('.
    pairs = {')':'(', ']':'[', '}':'{'}

    for ch in expression:
        # ---- A. OTWRCIE NAWIASU ----
        if ch in "([{":
            # Wrzucamy na stos (zapamiętujemy: "hej, otworzyłem nawias, czekam na parę").
            stack.put(ch)

        # ---- B. ZAMKNIĘCIE NAWIASU ----
        elif ch in ")]}":
            # Błąd 1: Chcemy zamknąć nawias, ale stos jest pusty (czyli nic nie otworzyliśmy).
            if stack.empty():
                return False
            
            # Błąd 2: Sprawdzamy parę. .get() pobiera ostatni otwarty nawias ze stosu.
            # Jeśli np. zamykasz ']', a na stosie czeka '(', to jest błąd.
            if stack.get() != pairs[ch]:
                return False

    # ---- C. KONIEC SPRAWDZANIA ----
    # Jeśli stos jest pusty = wszystkie nawiasy zostały ładnie zamknięte -> PRAWDA.
    # Jeśli coś zostało na stosie = brakuje zamknięcia (np. "((2+2") -> FAŁSZ.
    return stack.empty()

for e in [expression1, expression2, expression3]:
    print(e, "OK" if brackets_ok(e) else "INVALID")