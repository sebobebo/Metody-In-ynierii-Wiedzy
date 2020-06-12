from zadania.zadanie2.file_manager.file_manager import FileManager

f = FileManager('test.txt')

f.update_file('Dodajemy1')
f.update_file('Dodajemy2')
f.update_file('\nDodajemy3')

print(f.read_file())