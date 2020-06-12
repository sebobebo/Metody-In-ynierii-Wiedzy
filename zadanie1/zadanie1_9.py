studenci = [('Jan', 'Kowalski', 198451), ('Adam', 'Strzała', 198574), ('Karolina', 'Musiał', 199661), ('Rafał', 'Bordowski', 192978), ('Jan', 'Strządała', 196666)]
print('lista studentow: ', studenci)

studenci_2 = []
for student in studenci:
    slownik = dict()
    slownik['imie'] = student[0]
    slownik['nazwisko'] = student[1]
    slownik['indeks'] = student[2]
    studenci_2.append(slownik)

print('w slowniku', studenci_2)

studenci_2[0]['wiek'] = 20
studenci_2[0]['adres_email'] = 'email@wp.pl'
studenci_2[0]['rok_urodzenia'] = '1994'
studenci_2[0]['adres'] = 'pl. Wolnosci 21'

studenci_2[1]['wiek'] = 21
studenci_2[1]['adres_email'] = 'ptaki12@wp.pl'
studenci_2[1]['rok_urodzenia'] = '1993'
studenci_2[1]['adres'] = 'ul. Ptasia 5'

studenci_2[2]['wiek'] = 22
studenci_2[2]['adres_email'] = 'email2@wp.pl'
studenci_2[2]['rok_urodzenia'] = '1992'
studenci_2[2]['adres'] = 'ul. Piastowska 1'

studenci_2[3]['wiek'] = 23
studenci_2[3]['adres_email'] = 'krowy555@wp.pl'
studenci_2[3]['rok_urodzenia'] = '1991'
studenci_2[3]['adres'] = 'ul. Krowia 15'

studenci_2[4]['wiek'] = 24
studenci_2[4]['adres_email'] = 'brzechwa5@wp.pl'
studenci_2[4]['rok_urodzenia'] = '1990'
studenci_2[4]['adres'] = 'pl. Skargi 21'

print('dodatkowe dane:', studenci_2)