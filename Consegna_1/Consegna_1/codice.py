import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importiamo i dati con la libreria pandas
df = pd.read_excel("Meteo_Chioggia60.ods", engine="odf", header=3)
df.columns = ['Data', 'Tmin', 'Tmed', 'Tmax', 'Ptot']
df = df.dropna()

# Funzione per calcolare i valori ottimali (minimi) di a e b
def minimi(x, y):
    
    x_mean = np.mean(x) #media campionaria di x
    y_mean = np.mean(y) #media campionaria di y
    
    # Calcolo di a => covarianza / varianza
    covarianza = np.sum((x - x_mean) * (y - y_mean))
    varianza = np.sum((x - x_mean)**2)
    a_ottimo = covarianza / varianza
    
    # Calcolo di b => media campionaria di y - a * media campionaria di x
    b_ottimo = y_mean - a_ottimo * x_mean
    
    return a_ottimo, b_ottimo



#Eseguiamo la funzione sui due campioni bi-variati
coppie = [('Tmin', 'Tmed'), ('Tmin', 'Ptot')]

for col_x, col_y in coppie:
    
    # Estraiamo i dati per x e y: 
    # x e y sono array numpy di valori float
    x = df[col_x].values.astype(float)
    y = df[col_y].values.astype(float)
    
    # Calcoliamo i valori ottimali di a e b
    a_star, b_star = minimi(x, y)
    
    # Grafico dei dati e della retta di regressione
    y_pred = a_star * x + b_star
    plt.scatter(x, y, label="Dati osservati", color="blue")
    plt.plot(x, y_pred, label=f"Retta di regressione: y = {a_star:.2f}x + {b_star:.2f}", color="red")
    plt.plot([], [], ' ', label=f"Valori: a = {a_star:.2f}, b = {b_star:.2f}") #valori espliciti di a e b
    
    #Plotting
    plt.xlabel(col_x)
    plt.ylabel(col_y)
    plt.legend()
    plt.title(f"Regressione lineare: {col_x} vs {col_y}")
    plt.grid()
    plt.show()
    
    
#Seconda parte: matrice di covarianza e componenti principali
#Costruiamo il campione con i dati delle colonne (Tmin, Tmed, Tmax, Ptot)
campione = df[['Tmin', 'Tmed', 'Tmax', 'Ptot']].values.astype(float)

#Matrice di covarianza
cov_matrix = np.cov(campione, rowvar=False) # rowvar=False: le colonne sono le variabili

#Autovalori e autovettori
autovalori, autovettori = np.linalg.eig(cov_matrix)
idx = np.argsort(autovalori)[::-1]  # Indici degli autovalori ordinati in senso decrescente
autovalori_ordinati = autovalori[idx]
autovettori_ordinati = autovettori[:, idx]

# Matrice di covarianza
cov_matrix = np.cov(campione, rowvar=False)

# Autovalori e autovettori
autovalori, autovettori = np.linalg.eig(cov_matrix)
idx = np.argsort(autovalori)[::-1]  
autovalori_ordinati = autovalori[idx]
autovettori_ordinati = autovettori[:, idx]

# Aggiunta per stampare le matrici
print("Matrice diagonale degli autovalori ordinati:")
print(np.diag(autovalori_ordinati))
print("\nMatrice ortonormale degli autovettori ordinati:")
print(autovettori_ordinati)

# Autovettori principali => componenti principali
autovettori_principali = autovettori_ordinati[:, :2]
# Autovettori principali => componenti principali
autovettori_principali = autovettori_ordinati[:, :2]

# Proiettiamo i dati originali sulle due direzioni principali
componenti_principali = campione @ autovettori_principali # Prodotto matrice per matrice

# Grafico di dispersione delle prime due componenti
plt.scatter(componenti_principali[:, 0], componenti_principali[:, 1], color='blue', alpha=0.7)
plt.xlabel("Prima componente")
plt.ylabel("Seconda componente")
plt.title("Grafico di dispersione delle prime due componenti principali")
plt.grid()
plt.show()
