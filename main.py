plik = open('in.txt', "a")
if plik.writable():
    plik.write(input('Podaj tekst: ') + "\n")
plik.close()


plik = open('in.txt', 'r')

if plik.readable():
    print("Zawartosc pliku: ")
    tekst = plik.read()
    print(tekst)

if plik.readable():
    print("Zawartosc pliku: ")
    tekst = plik.readlines()
    print(tekst)
    for l in tekst:
        print()

# class magazyn:
#     def __init__(self):
#         self.sprzedaz = {}
#
#     def wczytaj_zawartosc(self, sciezka_do_pliku):
#         with open(sciezka_do_pliku, 'r') as f:
#             while True:


