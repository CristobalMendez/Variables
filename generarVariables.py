import numpy as np
import json
import pandas as pd

# Generar un conjunto de datos aleatorios solo para ScaledTimeAlive
def generar_variables_prueba(num_samples=10):
    """
    Genera un conjunto de datos aleatorios solo para ScaledTimeAlive.
    
    :param num_samples: Número de muestras a generar.
    :return: DataFrame con la variable generada.
    """
    np.random.seed(42)  # Para reproducibilidad
    data = {
        "ScaledTimeAlive": np.random.uniform(0, 1, num_samples)  # Valores entre 0 y 1
    }
    return pd.DataFrame(data)

# Generar datos de prueba
data_prueba = generar_variables_prueba(num_samples=10)

# Guardar solo los valores de ScaledTimeAlive en un archivo JSON
def guardar_variables_json(data, filename="variables.json"):
    """
    Guarda las variables independientes en un archivo JSON.
    
    :param data: DataFrame con las variables independientes.
    :param filename: Nombre del archivo JSON donde se guardarán los resultados.
    """
    resultados = []
    for index, row in data.iterrows():
        resultado = row.to_dict()  # Convierte la fila a un diccionario
        resultados.append(resultado)
    
    with open(filename, "w") as file:
        json.dump(resultados, file, indent=4)

# Guardar las variables en el archivo JSON
guardar_variables_json(data_prueba)

print(f"Las variables se han guardado en el archivo 'variables.json'.")
