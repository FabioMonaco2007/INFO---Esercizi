import random

print("QUADRATO MAGICO:")

def genera_matrice(n):
    """Genera una matrice n x n con numeri casuali che non si ripetono."""
    numeri = random.sample(range(1, n*n + 1), n*n)
    matrice = [numeri[i*n:(i+1)*n] for i in range(n)]
    return matrice

def verifica_quadrato_magico(matrice):
    """Verifica se la matrice è un quadrato magico."""
    n = len(matrice)
    costante_magica = sum(matrice[0])  #La somma della prima riga è la costante magica
    
    #Verifica righe
    for riga in matrice:
        if sum(riga) != costante_magica:
            return False, 0
    
    #Verifica colonne
    for i in range(n):
        if sum(matrice[j][i] for j in range(n)) != costante_magica:
            return False, 0
    
    #Verifica diagonale principale
    if sum(matrice[i][i] for i in range(n)) != costante_magica:
        return False, 0
    
    #Verifica diagonale secondaria
    if sum(matrice[i][n-i-1] for i in range(n)) != costante_magica:
        return False, 0
    
    return True, costante_magica

def stampa_matrice(matrice, costante_magica=None):
    """Stampa la matrice."""
    for riga in matrice:
        print("\t".join(map(str, riga)))
    if costante_magica is not None:
        print(f"Costante Magica: {costante_magica}")

def main():
    """Funzione principale."""
    for n in range(3, 11):  
        while True:
            matrice = genera_matrice(n)
            verifica, costante_magica = verifica_quadrato_magico(matrice)
            if verifica:
                stampa_matrice(matrice, costante_magica)
                break

if __name__ == "__main__":
    main()