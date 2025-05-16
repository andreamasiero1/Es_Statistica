import random
import matplotlib.pyplot as plt
import numpy as np

# Simula una singola partita
def simula_partita():
    pos = [0]*13        # pos[k] = riga attuale colonna k (ignoriamo pos[0])
    mosse = 0
    while True:
        mosse += 1
        # Lancia due dadi
        s = random.randint(1,6) + random.randint(1,6)
        if 1 <= s <= 12:  # Controllo che s sia nel range valido (in realtà sempre vero con due dadi)
            pos[s] += 1  # la pedina in colonna s avanza
            # Controlla se questa colonna ha raggiunto la riga 19 (19 avanzamenti)
            if pos[s] >= 19:
                return s, mosse  # ritorna colonna vincente e numero di mosse

def main():
    # Imposta il seme per la riproducibilità dei risultati
    random.seed(42)
    
    # a)Calcolare la probabilità che la colonna 7 vinca prima della colonna 8
    # => simulazione specifica
    simulazioni_7_vs_8 = 100000
    vittorie_7 = 0
    
    for _ in range(simulazioni_7_vs_8):
        pos = [0] * 13
        while pos[7] < 19 and pos[8] < 19:  # Continua finché né 7 né 8 hanno vinto
            s = random.randint(1, 6) + random.randint(1, 6)
            if 1 <= s <= 12:
                pos[s] += 1
        
        # Se 7 ha vinto (raggiunto o superato riga 19) e 8 non ha vinto
        if pos[7] >= 19 and pos[8] < 19:
            vittorie_7 += 1
    
    prob_7_prima_di_8 = vittorie_7 / simulazioni_7_vs_8
    print(f"\na) P(Colonna 7 vince prima di colonna 8) = {prob_7_prima_di_8:.6f}\n\n")
    
    
    #Altri punti della traccia: ciclo sulle partite
    # Numero di simulazioni
    simulazioni = 100000
    win_count = [0]*13 #ignoriamo la prima colonna
    durate = [] #memorizziamo le durate delle partite
    
    # b) Esegui tutte le simulazioni
    for _ in range(simulazioni):
        vincitore, N = simula_partita()
        win_count[vincitore] += 1 #aumentiamo il win count della colonna vincente
        durate.append(N)

    # Calcola probabilità di vittoria per colonna k
    prob_vittoria = [win_count[k]/simulazioni for k in range(13)]

    # c) Calcola P(T=N) per N fino a 200 
    freq_T = {}
    for N in durate:
        freq_T[N] = freq_T.get(N, 0) + 1
    prob_T = {N: freq_T.get(N, 0)/simulazioni for N in range(1, 201)}

    # d) Il gioco ha durata di più di 100 mosse
    prob_più_di_100 = sum(freq_T.get(N, 0) for N in range(101, max(durate) + 1)) / simulazioni
    
    # e) Il gioco ha durata di più di 200 mosse
    prob_più_di_200 = sum(freq_T.get(N, 0) for N in range(201, max(durate) + 1)) / simulazioni
    
    # Calcola la durata media del gioco
    durata_media = sum(durate) / len(durate)
    
    # Stampa i risultati
    print("Risultati basati su", simulazioni, "simulazioni:")
    print("\nb) Probabilità di vittoria delle colonne k=1..12:")
    for k in range(1, 13):
        print(f"P(Colonna {k} vince) = {prob_vittoria[k]:.6f}")
        
    print("\nc) Probabilità che una partita duri esattamente N mosse:")
    for N in range(1, 201):
        print(f"P(T={N}) = {prob_T[N]:.6f}")
    
    print(f"\nd) P(durata > 100 mosse) = {prob_più_di_100:.6f}")
    print(f"e) P(durata > 200 mosse) = {prob_più_di_200:.6f}")
    print(f"\nDurata media del gioco: {durata_media:.2f} mosse")
    
    # Grafico della probabilità di vittoria per colonna k
    #plt.figure(figsize=(10, 6))
    #colonne = list(range(1, 13))
    #plt.bar(colonne, prob_vittoria[1:13], color='steelblue')
    #plt.xlabel('Colonna k')
    #plt.ylabel('Probabilità di vittoria')
    #plt.title('Probabilità che la pedina in colonna k arrivi per prima')
    #plt.xticks(colonne)
    #plt.grid(axis='y', linestyle='--', alpha=0.7)
    #plt.savefig('prob_vittoria_colonne.pdf')
    
    # Grafico della probabilità di durata esatta N mosse
    #plt.figure(figsize=(12, 6))
    #N_values = list(range(1, 201))
    #prob_values = [prob_T[N] for N in N_values]
    #plt.plot(N_values, prob_values, color='darkred', linewidth=1.5)
    #plt.xlabel('Numero di mosse N')
    #plt.ylabel('Probabilità')
    #plt.title('Probabilità che il gioco abbia durata di esattamente N mosse')
    #plt.grid(True, linestyle='--', alpha=0.7)
    #plt.savefig('prob_durata_N_mosse.pdf')
    
    
    
if __name__ == "__main__":
    main()