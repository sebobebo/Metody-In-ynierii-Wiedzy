# Pkt. 1
tekst = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker".lower()
litera_1 = 'a'
litera_2 = 'b'
liczba_liter_1 = tekst.count(litera_1)
liczba_liter_2 = tekst.count(litera_2)
print("W tekście jest {0} liter {1} oraz {2} liter {3}".format(liczba_liter_1, litera_1, liczba_liter_2, litera_2))

