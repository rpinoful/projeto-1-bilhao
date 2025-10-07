from csv import reader
from pathlib import Path
from collections import defaultdict
import time
from pprint import pprint
from itertools import islice

temperatura_por_station = defaultdict(list)

#configurando path dinamico
path_do_csv = Path("data") / "weather_stations.csv"

start_time = time.time()

#lectura del archivo
with open(path_do_csv, 'r', encoding='utf-8') as file:
    _reader = reader(file, delimiter=';')  # Nota: solo reader
    
    
# Percorre el archivo csv almacenada en la variavel e retorna su contenido    
    for row in _reader:
        if len(row)<2:
            continue
        nome_station = row[0] #pega o nome da estação
        temperatura = float(row[1]) #pega o valor da temperatura e transforma em float
        temperatura_por_station[nome_station].append(temperatura)
    


# dicionario armazena resultados
results = {}    

# itera o dicionario que contem Stations[temp1,temp2,temp3]
for station,temperatures in temperatura_por_station.items():
    min_temp = min(temperatures) #pega a temperatura minima na station atual
    max_temp = max(temperatures) #pega a temperatura maxima na station atual
    avg_temp = sum(temperatures)/len(temperatures) #calcula a media de temperaturas da station atual
    results[station] =(min_temp,max_temp,avg_temp)


#tempo que passou para processar
end_time = time.time() 
final_time = end_time - start_time

# Titulo do representando o projeto final
print("=" * 70) # coloca uma linha de 70 iguais
print("RELATÓRIO DE PROCESSAMENTO - CSV NATIVO") #titulo 
print("=" * 70) # coloca uma linha de 70 iguais


#Quantia de tempo que processou o codigo
print(f"Tempo total: {final_time:.2f} segundos")

#quantia de estações que processou 
print(f"Total de estações: {len(results)}")
print("=" * 70)


# Retornando as temperaturas alta , baixa e media do dicionario results

#1era forma list + slicing 
# for station,(min_temp,max_temp,avg_temp) in list(results.items())[:10]:
#     print(f"{station} : {min_temp:.1f} ºC / {avg_temp:.1f}ºC /{max_temp:.1f}ºC")


#2da forma com islice() (melhor forma mais limpa)
for station,(min_temp,max_temp,avg_temp) in islice(results.items(),100):
    print(f"{station} : {min_temp:.1f} ºC / {avg_temp:.1f}ºC /{max_temp:.1f}ºC")


