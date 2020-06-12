while True:
    print("Nowa gra")
    stol = 0
    nr_gracza = 1
    gra = True
    while gra:

        niepoprawna_wartosc = True
        while niepoprawna_wartosc == True:

            print("Gracz nr. " + str(nr_gracza))
            wartosc = input("Wybierz zeton: (dostepne wartosci to 4, 5, 6). Wpisz -1 aby zakonczyc")
            if wartosc == -1:
                exit(1)
            if wartosc <= 6 and wartosc >=4:
                niepoprawna_wartosc = False

        if nr_gracza ==1:
            nr_gracza = 2
        else:
            nr_gracza = 1
        stol += wartosc
        print("Wartosc stolu " + str(stol))
        if stol > 21:
            print("Gracz nr " + str(nr_gracza) + " wygral!")
            gra = False



