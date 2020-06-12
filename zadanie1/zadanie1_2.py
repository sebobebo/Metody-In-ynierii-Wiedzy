from datetime import datetime

print('{:>20}'.format('TEKST'))     # 20 komorek tekstu i wyrownanie do prawej
print('{:^20}'.format('TEKST'))     # 20 komorek tekstu i wysrodkowanie
print('{:.4f}'.format(3.141592653589793))       # tylko 4 liczby po przecinku
print('{:%d-%m-%Y %H:%M}'.format(datetime.now()))   # formatowanie daty i czasu
print('{:+d}'.format((-23)))    # wyswietlanie znaku liczby

