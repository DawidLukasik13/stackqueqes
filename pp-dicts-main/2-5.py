# ---- 1. DEFINICJA ZBIORÓW (SETS) ----
# Używamy nawiasów klamrowych {}, tak jak w słownikach, ale BEZ kluczy (nie ma par klucz:wartość).
# To są po prostu "worki" z unikalnymi napisami.

# Zbiór uprawnień, które są KONIECZNE, by wykonać zadanie.
required_permissions = {"read", "write", "execute"}

# Zbiór uprawnień, które POSIADA użytkownik.
user_permissions = {"read", "write"}

# ---- 2. SPRAWDZANIE ZAWIERANIA (SUBSET) ----
# Metoda .issubset() zadaje pytanie:
# "Czy WSZYSTKIE elementy ze zbioru po lewej (required) znajdują się w zbiorze po prawej (user)?"
# Innymi słowy: Czy użytkownik ma wszystko, czego wymagamy?
has_permissions = required_permissions.issubset(user_permissions)

# ---- 3. WYNIK ----
print(has_permissions)