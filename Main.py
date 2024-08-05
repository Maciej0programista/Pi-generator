import json
from decimal import Decimal, getcontext

# Ustawienie precyzji na 80000 cyfr po przecinku
getcontext().prec = 80000

# Obliczenie liczby Pi z zadaną precyzją
pi = Decimal(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679)

# Stworzenie słownika z cyfrą Pi
pi_dict = {
    "PI": str(pi)[2:]  # Pomiń "3."
}

# Zapisanie danych do pliku JSON
with open("PI.json", "w") as f:
    json.dump(pi_dict, f, indent=4)
