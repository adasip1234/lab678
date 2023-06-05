print("Program do konwersji danych obsługujący formaty: .xml, .json i .yml (.yaml)")
x = input("Podaj sciezke i rozszerzenie pliku: ")
y = input("Podaj sciezke i rozszerzenie pliku do jakiego chcialbys zapisac plik: ")
file_name, file_extension = os.path.splitext(x)
file_name_new, file_extension_new = os.path.splitext(y)

def sciezka():
    sciezka = os.path.isfile(x)
    if sciezka == True:
        print("Zaraz nastopi konwetrowanie ")
    else:
        print("Bledna sciezka pliku")
        quit()
    return x, y
