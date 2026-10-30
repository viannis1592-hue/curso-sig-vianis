
import json

# 1. Definir la ruta del archivo GeoJSON
ruta = r"C:\Users\viann\curso-sig\datos\provincias_boyaca.geojson"

# 2. Abrir y leer el archivo
with open(ruta, "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

# 3. Crear un diccionario vacío para contar municipios
conteo = {}

# 4. Recorrer los municipios del GeoJSON
for elemento in datos["features"]:
    provincia = elemento["properties"]["provincia"]

    # 5. Contar municipios por provincia
    if provincia in conteo:
        conteo[provincia] += 1
    else:
        conteo[provincia] = 1

# 6. Mostrar los resultados
print("MUNICIPIOS POR PROVINCIA")
print("------------------------")

for provincia, cantidad in sorted(conteo.items()):
    print(f"{provincia}: {cantidad} municipios")

print("------------------------")
print("Total de municipios:", sum(conteo.values()))
