
import pandas as pd
from generate_history_data_microservice import create_data
from predictions import generar_analisis
from assets import financial_asset_info
import os
import time
from datetime import datetime
import streamlit as st

from tensorflow.keras.models import load_model
model_final = load_model('modelos_redes/model_3-A_binance_1m_5x1_2.0.h5')



if __name__== "__main__":
    # Título
    html_temp = """
    <h1 style="color:#181082;text-align:center;">SISTEMA DE PREDICCION PARA TRADING </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    

    # Lecctura de datos
    temp_formulario = st.radio( "Escoja la temporalidad de la operación:",('1m', '5m', '15m'))
    numero_predicciones = st.number_input('Ingrese el número de prediciones', min_value=1, max_value=100000, value=3,step=1)


    num_predictions = numero_predicciones
    interval_time = temp_formulario
    timer = 60 #tiempo en segundos de espera para solicitar informacion



    # #se crea boton para iniciar la ejecución
    if st.button("Iniciar trading"):
 
        t_inicial = time.time()

        ### evaluation
        for i in range(0,num_predictions):
                    
            num_data = 1  # se crea nuevo dato para analizar 
            create_data(num_data, timer, interval_time,financial_asset_info)

            times,nombres_acciones,sumary,moving_averages,oscillators,indicators = generar_analisis(model_final,interval_time)

            data = {
                'time': str(times),
                'acciones': nombres_acciones,
                'sumary': sumary,
                'moving_averages': moving_averages,
                'oscillators': oscillators,
                'indicators': indicators
            }

            df = pd.DataFrame(data)
            
            folder = 'results_history'
            file = f'results_{interval_time}.xlsx'
            path = os.path.join(folder, file)

            if os.path.exists(path):
                df_existing = pd.read_excel(path)
                df = pd.concat([df_existing, df], ignore_index=True)
            df.to_excel(path, index=False)


            ###visualization
            st.success(f"PREDICTION: {i+1} - TEMPORALIDAD: {interval_time} --- {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            df1 = pd.DataFrame(
                data,
                columns=["times","acciones","sumary","moving_averages","oscillators","indicators"]
            )
            st.dataframe(df1)


            ### Espera n segundos antes del próximo ciclo
            mult = int(interval_time.replace("m", ""))
            time.sleep(time_seg*mult) ### falta hacer multiplicador por interval_time


        t_final = time.time()
        times = round(t_final-t_inicial, 3)
        print(f"tiempo de ejecucion TOTAL: {times} seg")
        st.success(f"tiempo de ejecucion TOTAL: {times} seg")