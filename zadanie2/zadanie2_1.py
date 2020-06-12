def funkcja1(a_list, b_list):
    wynik = []
    for indeks in range(0, len(a_list), 2):
        wynik.append(a_list[indeks])
    for indeks in range(1, len(b_list), 2):
        wynik.append(b_list[indeks])
    return wynik

print(funkcja1([0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12, 13]))
