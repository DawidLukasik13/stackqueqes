import queue

n = int(input("Natural number: "))

# ---- 1. PRZYGOTOWANIE STOSU ----
# LifoQueue (Last In, First Out).
# Dlaczego stos? Bo reszty z dzielenia pojawiają się w kolejności odwrotnej
# do tej, w jakiej czytamy liczbę binarną.
stack = queue.LifoQueue()
num = n

# ---- 2. OBLICZANIE RESZT (ZAPIS NA STOS) ----
while num > 0:
    # Krok A: Oblicz resztę z dzielenia przez 2 (to będzie 0 lub 1).
    # To jest nasza cyfra binarna.
    remainder = num % 2
    
    # Krok B: Wrzucamy cyfrę na stos.
    # Pierwsza wyliczona cyfra ląduje na DNIE stosu (będzie ostatnia).
    stack.put(remainder)
    
    # Krok C: Dzielimy liczbę całkowicie przez 2 (ucinamy resztę).
    # Np. 13 // 2 = 6 (a nie 6.5).
    num //= 2

# ---- 3. ODCZYT ZE STOSU (ODWRÓCENIE) ----
binary = ""

# Zdejmujemy elementy dopóki stos nie jest pusty.
while not stack.empty():
    # .get() pobiera element z WIERZCHU stosu (czyli ten dodany jako ostatni).
    # Dzięki temu odwracamy kolejność cyfr:
    # Ostatnia obliczona reszta staje się pierwszą cyfrą liczby binarnej.
    binary += str(stack.get())

print("Binary number:", binary)