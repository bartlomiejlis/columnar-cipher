# Zmiennej "szyfrogram" przypisujemy jako początkową wartość łańcuch pusty (ang. empty string), czyli łancuch bez znaków (o długości 0). Łańcuch ten będziemy wydłużać o kolejne znaki szyfrogramu.
szyfrogram = ""

jawny = input("Podaj tekst jawny (bez spacji): ")
klucz = int(input("Podaj klucz szyfrowania: "))

# Obliczamy długość tekstu jawnego
dl = len(jawny)

for i in range(0, klucz):
    for j in range(i, dl, klucz):
        # Napis aktualnie przechowywany w zmiennej "szyfrogram" powiększamy z prawej strony o kolejny znak z wykorzystaniem operacji złączenia
        szyfrogram = szyfrogram + jawny[j]

print("\nSzyfrogram:", szyfrogram)