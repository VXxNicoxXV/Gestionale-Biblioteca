from menu import Menu
from registra_utente import dati_utente

def main():
    numero_tessera = 1
    clienti = []
    while True:
        Menu.mostra_menu()
        scelta = input("Inserisci la tua scelta: ")
        match scelta:
            case "1":
                utente = dati_utente(numero_tessera)
                clienti.append(utente)
                print(clienti)
                numero_tessera += 1
                
            case _:
                continue

    













if __name__ == "__main__":
    main()