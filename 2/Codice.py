import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Numero totale di elettori (N + M = 10^6)
N_M_totale = int(1e6)

# Valori di M (numero di sostenitori di A) da 0 a 5000 con passo 10
M = np.arange(0, 5001, 10)  # M = numero di sostenitori di A

# Lista per memorizzare le probabilità calcolate
probabilità = []

# Iterazione sui possibili valori di M (sostenitori di A)
for M_corrente in M:
    # Calcolo di N (numero di elettori indecisi)
    N = N_M_totale - M_corrente
    
    # Calcolo della soglia: numero minimo di voti dagli indecisi che servono ad A per vincere
    soglia = (N - M_corrente) // 2 + 1  # t_start
    
    # Approssimiamo la distribuzione binomiale (successi tra gli indecisi) con una normale
    # perché N è molto grande. 
    # (Abbiamo scoperto che è un procedimento che spesso si fa in statistica per semplificare i calcoli).
    media = N * 0.5  # Valore atteso di successi (probabilità 0.5 per ogni indeciso)
    deviazione_std = np.sqrt(N * 0.25)  # Deviazione standard della binomiale
    
    # Calcoliamo lo z-score: quante deviazioni standard la soglia è distante dalla media
    # Usiamo la correzione di continuità (-0.5) perché la binomiale è discreta e la normale è continua
    z = (soglia - 0.5 - media) / deviazione_std
    
    # Calcoliamo la probabilità che A vinca, ovvero ottenga almeno la soglia di voti dagli indecisi
    # (cioè la probabilità che una normale standard sia maggiore di z)
    probabilità_vittoria = 1 - norm.cdf(z)
    probabilità.append(probabilità_vittoria)
    
    # Stampa per vedere i risultati passo passo
    print(f"M (sostenitori) = {M_corrente}, N (indecisi) = {N}, Probabilità di vittoria di A = {probabilità_vittoria:.6f}")

# Generazione del grafico
plt.figure(figsize=(10, 6))
plt.plot(M, probabilità, 'b-', label='Probabilità di vittoria di A')
plt.xlabel('M (Numero di sostenitori di A)')
plt.ylabel('Probabilità di vittoria di A')
plt.title('Probabilità di vittoria di A al variare di M')
plt.grid(True)
plt.legend()
#plt.savefig('probability_plot.pdf', format='pdf')
plt.show()
