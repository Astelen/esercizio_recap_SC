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

