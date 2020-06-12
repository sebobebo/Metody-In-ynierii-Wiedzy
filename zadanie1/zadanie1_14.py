dane = [{'imie': 'Jan', 'nazwisko': 'Kowalski', 'indeks': 198451, 'wiek': 20, 'adres_email': 'email@wp.pl', 'rok_urodzenia': '1994', 'adres': 'pl. Wolnosci 21', 'srednia': 4.2135}, {'imie': 'Adam', 'nazwisko': 'Strzała', 'indeks': 198574, 'wiek': 21, 'adres_email': 'ptaki12@wp.pl', 'rok_urodzenia': '1993', 'adres': 'ul. Ptasia 5', 'srednia': 3.124787}, {'imie': 'Karolina', 'nazwisko': 'Musiał', 'indeks': 199661, 'wiek': 22, 'adres_email': 'email2@wp.pl', 'rok_urodzenia': '1992', 'adres': 'ul. Piastowska 1', 'srednia': 4.893135}, {'imie': 'Rafał', 'nazwisko': 'Bordowski', 'indeks': 192978, 'wiek': 23, 'adres_email': 'krowy555@wp.pl', 'rok_urodzenia': '1991', 'adres': 'ul. Krowia 15', 'srednia': 4.5555}, {'imie': 'Jan', 'nazwisko': 'Strządała', 'indeks': 196666, 'wiek': 24, 'adres_email': 'brzechwa5@wp.pl', 'rok_urodzenia': '1990', 'adres': 'pl. Skargi 21', 'srednia': 3.8589}]

wynik = ''
for student in dane:
    wynik += '{s[imie]} {s[nazwisko]}:\n\tIndeks: {s[indeks]}\n\tWiek: {s[wiek]}\n\tEmail: {s[adres_email]}\n\tRok urodzenia: {s[rok_urodzenia]}\n\tAdres: {s[adres]}\n\tSrednia ocen: {s[srednia]:.2f}\n'.format(s=student)
print(wynik)
