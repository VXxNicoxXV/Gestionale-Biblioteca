from menu import Menu
from registra_utente import dati_utente
from registra_libro import dati_libro

def main():
    numero_tessera = 1
    clienti = []
    libri = []
    while True:
        Menu.mostra_menu()
        scelta = input("Inserisci la tua scelta: ")
        match scelta:
            case "1":
                utente = dati_utente(numero_tessera)
                clienti.append(utente)
                print(clienti)
                numero_tessera += 1

            case "2":
                libro = dati_libro()
                libri.append(libro)
                print(libri)
            case _:
                continue

    













if __name__ == "__main__":
    main()