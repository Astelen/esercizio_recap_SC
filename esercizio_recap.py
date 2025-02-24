##Esercizio slide 324, punto 1

import numpy as np
import pandas as pd
from numpy import sqrt
import matplotlib.pyplot as plt

#Creo array di dati grezzi
giorni = 305
pazienti_medi = 1200
dev_st = 900
dati_grezzi = np.random.normal(pazienti_medi, dev_st, giorni)
dati_grezzi

#Creo trend crescente
trend_crescente = np.linspace(pazienti_medi - dev_st, pazienti_medi + dev_st, 305)
trend_crescente

#Unisco distribuzione normale con trend crescente
dati_con_trend = dati_grezzi - trend_crescente
dati_con_trend

#Molti dati risultano negativi, quindi aggiungo il clip per segnare un valore minimo oltre il quale non andare
dati_con_trend = np.clip(dati_con_trend, a_min=300, a_max=None)
dati_con_trend


##Esercizio punto 2

#Creo range di date
date_range = pd.date_range(start='2024-01-01', periods=giorni, freq='D')
date_range

# #Creo colonna con patologia casuale
patologia = ['osteoporosi', 'infarto', 'danno neurologico']
colonna_patologie = np.random.choice(patologia, giorni, replace=True)
colonna_patologie

#Creazione Database
df = pd.DataFrame ({
    'Data': date_range,
    'Visitatori': dati_con_trend,
    'Patologia': colonna_patologie
                    })
df.head()
df.describe()
df.info()



##Esercizio punto 3
#Estraggo anno e mese
df['Anno'] = pd.DatetimeIndex(df['Data']).year
df['Mese'] = pd.DatetimeIndex(df['Data']).month
df.info()

#Calcolo media per mese
visitatori_mean = df.groupby('Mese')['Visitatori'].mean()
visitatori_mean

#Calcolo dev. st.
visitatori_std = df.groupby('Mese')['Visitatori'].std()
visitatori_std

#Conteggio di tutti i valori per visualizzare valore piu' frequente, valore meno frequente
df['Patologia'].value_counts()