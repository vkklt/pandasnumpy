import numpy as np
import pandas as pd

df = pd.read_csv('bike-sharing.csv', sep=',')

print("o tamanho do dataset é: ", df.shape)

print("a média de windspeed é: ", df['windspeed'].mean())

print("a média de temp é: ", df['temp'].mean())

df['datetime'] = pd.to_datetime(df['datetime'], format='%Y-%m-%d')
print ("o ano 2011 tem: ", df[df['datetime'].dt.year == 2011].shape[0], "registros")
print ("o ano 2012 tem: ", df[df['datetime'].dt.year == 2012].shape[0], "registros")

bike2011 = df.loc[df['datetime'].dt.year == 2011]
bike2012 = df.loc[df['datetime'].dt.year == 2012]
print("o total de bicicletas em 2011 é: ", bike2011['total_count'].sum())
print("o total de bicicletas em 2012 é: ", bike2012['total_count'].sum())

medias = [df[df['season'] == 1]['total_count'].mean(), df[df['season'] == 2]['total_count'].mean(), df[df['season'] == 3]['total_count'].mean(), df[df['season'] == 4]['total_count'].mean()]
max_medias = medias.index(max(medias)) + 1
min_medias = medias.index(min(medias)) + 1

if min_medias  == 1: min = "verão"
if min_medias  == 2: min = "outono"
if min_medias  == 3: min = "inverno"
if min_medias  == 4: min = "primavera"

if max_medias  == 1: max = "verão"
if max_medias  == 2: max = "outono"
if max_medias  == 3: max = "inverno"
if max_medias  == 4: max = "primavera"

print("a estação do ano com mais aluguel é: ", max)
print("a estação do ano com menos aluguel é: ", min)

horas = df.groupby('hour')['total_count'].mean()
horaComMaisAluguel = horas.idxmax()
print("A hora com mais aluguéis é:", horaComMaisAluguel, "horas")

horas = df.groupby('hour')['total_count'].mean()
horaComMenosAluguel = horas.idxmin()
print("A hora com menos aluguéis é:", horaComMenosAluguel, "horas")

dias = df.groupby('weekday')['total_count'].mean()
diaComMaisAluguel = dias.idxmax()
diaComMenosAluguel = dias.idxmin()

if diaComMaisAluguel == 0: diaMax = "domingo"
if diaComMaisAluguel == 1: diaMax = "segunda"
if diaComMaisAluguel == 2: diaMax = "terça"     
if diaComMaisAluguel == 3: diaMax = "quarta" 
if diaComMaisAluguel == 4: diaMax = "quinta" 
if diaComMaisAluguel == 5: diaMax = "sexta" 
if diaComMaisAluguel == 6: diaMax = "sabado" 

if diaComMenosAluguel == 0: diaMin = "domingo"
if diaComMenosAluguel == 1: diaMin = "segunda"
if diaComMenosAluguel == 2: diaMin = "terça"
if diaComMenosAluguel == 3: diaMin = "quarta"
if diaComMenosAluguel == 4: diaMin = "quinta"
if diaComMenosAluguel == 5: diaMin = "sexta"
if diaComMenosAluguel == 6: diaMin = "sabado"

print("O dia da semana com mais aluguéis é:", diaMax)
print("O dia da semana com menos aluguéis é:", diaMin)

quarta = df.loc[df['weekday'] == 3]
horas = quarta.groupby('hour')['total_count'].mean()
horaComMaisAluguel = horas.idxmax()
print("A hora com mais aluguéis na quarta feira é:", horaComMaisAluguel, "horas")

sabado = df.loc[df['weekday'] == 6]
horas = sabado.groupby('hour')['total_count'].mean()
horaComMaisAluguel = horas.idxmax()
print("A hora com mais aluguéis no sábado é:", horaComMaisAluguel, "horas")












