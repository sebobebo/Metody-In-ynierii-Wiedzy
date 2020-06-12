def funkcja(temperature, temperature_type):
    wynik = 0
    if temperature_type == 'Fahrenheit':
        return temperature * 1.8 + 32.0
    elif temperature_type == 'Rankine':
        return temperature * 1.8 + 491.67
    elif temperature_type == 'Kelvin':
        return temperature - 273.15
    else:
        return 'Nieprawidlowe dane'


print('Fahrenheit;', funkcja(25, 'Fahrenheit'))
print('Rankine;', funkcja(25, 'Rankine'))
print('Kelvin;', funkcja(25, 'Kelvin'))
