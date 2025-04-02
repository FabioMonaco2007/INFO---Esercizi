#Nome: Fabio Monaco
#Partner: Jason Mezzadri

import random

# Funzione per lanciare i dadi
def lancia_dadi(armate):
    return sorted([random.randint(1, 6) for _ in range(armate)], reverse=True)

# Funzione per eseguire il combattimento
def combatti(attaccante, difensore):
    while attaccante > 0 and difensore > 0:
        # Determina il numero di armate da attaccante e difensore (max 3)
        num_attacco = min(3, attaccante)
        num_difesa = min(3, difensore)
        
        print(f"\nArmata attaccante: {attaccante}, armata difensore: {difensore}")
        print(f"Numero di armate attaccanti che partecipano: {num_attacco}")
        print(f"Numero di armate difensive che partecipano: {num_difesa}")
        
        # Lancio dei dadi
        dadi_attaccante = lancia_dadi(num_attacco)
        dadi_difensore = lancia_dadi(num_difesa)
        
        print(f"Dadi attaccante: {dadi_attaccante}")
        print(f"Dadi difensore: {dadi_difensore}")
        
        # Confronto dei dadi
        for i in range(min(num_attacco, num_difesa)):
            if dadi_attaccante[i] > dadi_difensore[i]:
                print(f"Attaccante vince il confronto {dadi_attaccante[i]} vs {dadi_difensore[i]}")
                difensore -= 1
            else:
                print(f"Difensore vince il confronto {dadi_difensore[i]} vs {dadi_attaccante[i]}")
                attaccante -= 1

        print(f"Armate attaccante: {attaccante}, armate difensore: {difensore}")
        if attaccante == 0 or difensore == 0:
            break

    # Risultato finale
    if attaccante > difensore:
        print("L'attaccante ha vinto!")
    elif difensore > attaccante:
        print("Il difensore ha vinto!")
    else:
        print("La battaglia è finita in pareggio!")

# Funzione principale
def main():
    # Estrazione casuale del numero di armate tra 7 e 12 per l'attaccante e il difensore
    attaccante = random.randint(7, 12)
    difensore = random.randint(7, 12)
    
    print(f"Armata attaccante: {attaccante}, armata difensore: {difensore}")
    
    # Esecuzione del combattimento
    combatti(attaccante, difensore)

# Esecuzione dello script
if __name__ == "__main__":
    main()