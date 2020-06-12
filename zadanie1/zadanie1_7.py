lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nowa_lista = lista[5:]
lista = lista[:5]

print('oryginalna lista:', lista)
print('nowa lista:', nowa_lista)

lista = [0] + lista + nowa_lista
lista.sort(reverse=True)
print('polaczona i posortowana lista:', lista)
