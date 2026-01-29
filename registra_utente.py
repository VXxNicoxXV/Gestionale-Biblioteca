class Registrazione:
    def __init__(self, nome_utente, cognome_utente, numero_utente):
        self.nome = nome_utente
        self.cognome = cognome_utente
        self.numero = numero_utente
        self.prestiti = 0
    
    def __repr__(self):
        return f"Cliente {self.nome} {self.cognome} numero: {self.numero}, attualmente ha in prestito {self.prestiti} libri"


def dati_utente(numero_tessera):
    print("Adesso dovrai inserire i tuoi dati")
    while True:
        nome_utente = input("Inserisci il tuo nome: ")
        cognome_utente = input("Inserisci il tuo cognome: ")
        if not nome_utente.isalpha() or not cognome_utente.isalpha():
            print("I dati inseriti non sono validi, reinseriscili")
            continue
        numero_utente = numero_tessera
        cliente = Registrazione(nome_utente, cognome_utente, numero_utente)
        return cliente


    