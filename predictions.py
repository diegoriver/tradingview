import numpy as np
import os
import json
import numpy as np
from datetime import datetime




X_velas = 5  # numero de flags para hacer el analisis la red neuronal



def tensor_flags(tabla_velas):
    """tabla_velas -> columns ('Open'[0], 'High'[1], 'Low'[2], 'Close[3]')"""
    """calcula la primera derivada de las velas (velocidad)"""
    flags_speed = np.array(tabla_velas[:, 3] - tabla_velas[:, 0])
    """calcula el valor maximo que alcanzó la vela"""
    flags_high = [tabla_velas[i, 1]-tabla_velas[i, 3] if flags_speed[i] >=
                  0 else tabla_velas[i, 1]-tabla_velas[i, 0] for i in range(len(tabla_velas))]
    """calcula el valor minimo que alcanzó la vela"""
    flags_low = [tabla_velas[i, 0]-tabla_velas[i, 2] if flags_speed[i] >=
                 0 else tabla_velas[i, 3]-tabla_velas[i, 2] for i in range(len(tabla_velas))]
    """calcula la segunda derivada (aceleracion) que alcanzó N numero de velas"""
    num_velas = X_velas  # numero de flags para hacer el analisis la red neuronal
    flags_aceleration = np.zeros(len(tabla_velas))
    for i in range(0, len(tabla_velas), num_velas):
        flags_aceleration[i:i+num_velas] = [(flags_speed[i+X_velas-1] - flags_speed[i])/X_velas]
    """crea el tensor de 4 filas dividiendolo el numero de columnas en n velas que se ingresan"""
    "une las listas por el eje de filas, creando una nueva dimension"
    arr = np.stack((flags_speed, flags_high, flags_low,
                   flags_aceleration), axis=0)
    "np.hsplit divide en varios arrays y np.array lo vuelve un solo array"
    a = len(arr[0])  # calcula la longitud de las columnas
    n = num_velas  # numero de velas que se desea agrupar para calcular el tensor
    tensor_final = np.array(np.hsplit(arr, a/n))
    return (tensor_final)


def data_train(tensores):
    "se crean los X_data "
    X_data = tensores.reshape(tensores.shape[0], tensores.shape[1]*tensores.shape[2])
    return (X_data)


def prediction(model_final, X_data):
    clasification = model_final.predict([X_data])
    umbral = 0.40
    clasification_final = ["buy" if i >= umbral else "sell" for i in clasification]
    return clasification_final



def generar_analisis(model_final,interval_time):
    # Usa os.listdir para obtener los nombres de todos los archivos en la carpeta
    archivos = os.listdir('data_history')
    nombres_filtrados = [nom for nom in archivos if nom.endswith(f'_{interval_time}.json')]

    nombres = []
    sumary =[]
    moving_averages =[]
    oscillators = []
    indicators_final = []
    times= []

    for nombre in nombres_filtrados:

        # Cargar el archivo JSON
        with open(f'data_history/{nombre}', 'r') as f:
            data = json.load(f)

        # Convertir las claves a datetime y ordenarlas
        keys = sorted(datetime.strptime(key, '%Y-%m-%d %H:%M:%S') for key in data.keys())
        # Seleccionar las últimas 5 claves
        last_five_keys = keys[-5:]
 
        sumary_recomendation = data[str(last_five_keys[-1])]['summary']['RECOMMENDATION']
        moving_averages_recomendation = data[str(last_five_keys[-1])]['moving_averages']['RECOMMENDATION']
        oscillators_recomendation = data[str(last_five_keys[-1])]['oscillators']['RECOMMENDATION']
        
        # try:
        #     indicators = []
        #     # Imprimir los últimos 5 elementos
        #     for key in last_five_keys:
        #         indicators.append( [data[str(key)]['indicators']['open'],\
        #                         data[str(key)]['indicators']['high'],\
        #                         data[str(key)]['indicators']['low'],\
        #                         data[str(key)]['indicators']['close'] ]
        #         )
        #     indicators = np.array(indicators)
        #     indicators = indicators[::-1] # se invierte el orden de la filas para que queden los valores actuales al principio}
        #     tensores = tensor_flags(indicators)
        #     X_data = data_train(tensores)

        #     indicators_recomendation = prediction(model_final, X_data) ### resultado de la prediccion
        # except:
        #     indicators_recomendation = "---"

        nombres.append(nombre.replace("results_", "").replace(f"_{interval_time}.json", ""))
        sumary.append(sumary_recomendation)
        moving_averages.append(moving_averages_recomendation)
        oscillators.append(oscillators_recomendation)
        # indicators_final.append(' '.join(indicators_recomendation))

        times.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        # print(times)
        # print(nombres)
    return times,nombres,sumary,moving_averages,oscillators # ,indicators_final