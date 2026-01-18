import queue

# ---- 1. TWORZENIE KOLEJKI FIFO ----
# queue.Queue() tworzy kolejkę typu FIFO.
# Wyobraź to sobie jak rurę: wrzucasz piłeczki z jednej strony, wypadają z drugiej.
# Nie możesz wyjąć piłeczki ze środka, musisz czekać na swoją kolej.
files_to_print = queue.Queue()

while True:
    print('1. Add file to print')
    print('2. Print file')
    print('0. Quit')
    menu = input('Select an option: ')
    
    # ---- 2. DODAWANIE PLIKU (PUT) ----
    if menu == '1':
        file_name = input('Enter file name to print: ')
        # .put() dodaje element na KONIEC kolejki (na koniec ogonka).
        files_to_print.put(file_name)

    # ---- 3. DRUKOWANIE (GET) ----
    elif menu == '2':
        # Sprawdzamy, czy kolejka nie jest pusta.
        # Gdybyśmy użyli .get() na pustej kolejce, program mógłby się "zawiesić" czekając na dane.
        if not files_to_print.empty():
            # .get() pobiera element z SAMEGO POCZĄTKU kolejki.
            # To jest kluczowa różnica względem stosu (LIFO).
            # Tu pobieramy "najstarszy" plik, a nie "najnowszy".
            file_to_print = files_to_print.get()
            print(f'File {file_to_print} is currently being printed. Please wait!')
        else:
            print('Queue empty!') # Nie ma nic do roboty

    elif menu == '0':
        break