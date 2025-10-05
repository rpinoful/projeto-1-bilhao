from csv import reader
from pathlib import Path

#configurando path dinamico
path_do_csv = Path("data") / "weather_stations.csv"


#lectura del archivo
with open(path_do_csv, 'r', encoding='utf-8') as file:
    _reader = reader(file, delimiter=';')  # Nota: solo reader
    
    
# Percorre el archivo csv almacenada en la variavel e retorna su contenido    
    for row in _reader:
        if len(row)<2:
            continue
        print(row)
        nome_station = row[0]
        temperatura = float(row[1])
        print(f"Estación: {nome_station}, Temperatura: {temperatura}")