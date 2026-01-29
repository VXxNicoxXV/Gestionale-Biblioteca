class Funzionalita:
    def cerca_libro(libri):
        trovati = []
        ricerca = input("Inserisci il titolo, l'ISBN o l'autore del libro: ")
        for libro in libri:
            if ricerca.lower() in libro.titolo.lower():
                trovati.append(libro)
            elif libro.isbn == ricerca:
                trovati.append(libro)
            elif libro.nome_autore.lower() == ricerca.lower():
                trovati.append(libro)
            elif libro.cognome_autore.lower() == ricerca.lower():
                trovati.append(libro)
            else:
                print("Libro non trovato!")
        return trovati
    
class Prestito:
    pass
    #Creazione di un nuovo oggetto prestito che associa i due oggetti Utente e Libro