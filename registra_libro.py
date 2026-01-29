class Libro:
    def __init__(self, titolo, nome_autore, cognome_autore, nazionalita_autore):
        self.titolo = titolo
        self.nome_autore = nome_autore
        self.cognome_autore = cognome_autore
        self.nazionalita_autore = nazionalita_autore
    
    def __repr__(self):
        return f"Titolo: {self.titolo}, Autore: {self.nome_autore} {self.cognome_autore}, Nazionalità: {self.nazionalita_autore}"
        

def dati_libro():
    print("Inserisci i dati del libro")
    while True:
        isbn = input("Inserisci l'ISBN del libro: ")
        while True:
            titolo = input("Inserisci il titolo del libro: ")
            if not titolo.isalpha():
                print("Titolo non valido")
                continue
            else:
                print("Dato inserito correttamente")
                break
        while True:
            nome_autore = input("Inserisci il nome dell'autore: ")
            if not nome_autore.isalpha():
                print("Nome non valido")
                continue
            else:
                print("Dato inserito correttamente")
                break
        while True:
            cognome_autore = input("Inserisci il cognome dell'autore: ")
            if not cognome_autore.isalpha():
                print("Cognome non valido")
                continue
            else:
                print("Dato inserito correttamente")
                break
        while True:
            nazionalita_autore = input("Inserisci la nazionalità dell'autore: ")
            if not nazionalita_autore.isalpha():
                print("Nazionalità non valida")
                continue
            else:
                print("Dato inserito correttamente: ")
                break
        libro = Libro(titolo, nome_autore, cognome_autore, nazionalita_autore)
        return libro



        