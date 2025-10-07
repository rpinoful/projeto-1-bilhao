from csv import reader
from pathlib import Path
from collections import defaultdict

temperatura_por_station = defaultdict(list)

#configurando path dinamico
path_do_csv = Path("data") / "weather_stations.csv"


#lectura del archivo
with open(path_do_csv, 'r', encoding='utf-8') as file:
    _reader = reader(file, delimiter=';')  # Nota: solo reader
    
    
# Percorre el archivo csv almacenada en la variavel e retorna su contenido    
    for row in _reader:
        if len(row)<2:
            continue
        nome_station = row[0]
        temperatura = float(row[1])
        temperatura_por_station[nome_station].append(temperatura)
    

# dicionario armazena resultados
results = {}    

# itera o dicionario que contem Stations[temp1,temp2,temp3]
for station,temperatures in temperatura_por_station.items():
    min_temp = min(temperatures) #pega a temperatura minima na station atual
    max_temp = max(temperatures) #pega a temperatura maxima na station atual
    avg_temp = sum(temperatures)/len(temperatures) #calcula a media de temperaturas da station atual
    results[station] =(min_temp,max_temp,avg_temp)   

print(list(results.items())[:5])




