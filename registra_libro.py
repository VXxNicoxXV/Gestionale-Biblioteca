class Libro:
    def __init__(self, titolo, nome_autore, cognome_autore, nazionalita_autore, isbn):
        self.titolo = titolo
        self.nome_autore = nome_autore
        self.cognome_autore = cognome_autore
        self.nazionalita_autore = nazionalita_autore
        self.isbn = isbn
    
    def __repr__(self):
        return f"Titolo: {self.titolo}, Autore: {self.nome_autore} {self.cognome_autore}, Nazionalità: {self.nazionalita_autore}"
        

def dati_libro():
    print("Inserisci i dati del libro")
    while True:
        isbn = input("Inserisci l'ISBN del libro: ")
        titolo = input("Inserisci il titolo del libro: ")
        print("Dato inserito correttamente")
        while True:
            nome_autore = input("Inserisci il nome dell'autore: ")
            if nome_autore.isdigit():
                print("Nome non valido")
                continue
            else:
                print("Dato inserito correttamente")
                break
        while True:
            cognome_autore = input("Inserisci il cognome dell'autore: ")
            if cognome_autore.isdigit():
                print("Cognome non valido")
                continue
            else:
                print("Dato inserito correttamente")
                break
        while True:
            nazionalita_autore = input("Inserisci la nazionalità dell'autore: ")
            if nazionalita_autore.isdigit():
                print("Nazionalità non valida")
                continue
            else:
                print("Dato inserito correttamente: ")
                break
        libro = Libro(titolo, nome_autore, cognome_autore, nazionalita_autore, isbn)
        return libro



        