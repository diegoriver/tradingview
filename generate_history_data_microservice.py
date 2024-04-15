### generate history data microservice

import json
import time
from tradingview_ta import TA_Handler
from datetime import datetime


# Define lOS ACTIVOS FINANCIEROS en una lista de diccionarios
financial_asset_info = [
    {
        "symbol": ["NVDA", "AAPL", "GOOG", "META", "MSFT", "TSLA", "AMZN"],
        "screener": "america",
        "exchange": "NASDAQ"
    },
    {
        "symbol": ["DOCN","BABA"],
        "screener": "america",
        "exchange": "nyse"
    },
    {
        "symbol": ["SPY", "VOO"],
        "screener": "america",
        "exchange": "AMEX"
    },
    {
        "symbol": ["GOLD"],
        "screener": "cfd",
        "exchange": "TVC"
    }
]

def create_data(num_data, time_seg, interval_time):
    for i in range(num_data):
        for info in financial_asset_info:
            for symbol in info["symbol"]:
                financial_asset = TA_Handler(
                    symbol=symbol,
                    screener=info["screener"],
                    exchange=info["exchange"],
                    interval=interval_time
                )

                result = {
                    'summary': financial_asset.get_analysis().summary,
                    'indicators': financial_asset.get_analysis().indicators,
                    'oscillators': financial_asset.get_analysis().oscillators,
                    'moving_averages': financial_asset.get_analysis().moving_averages
                }

                # Carga los resultados existentes, añadi el nuevo resultado y guarda
                try:
                    with open(f'data_history/results_{symbol}_{interval_time}.json', 'r') as f:
                        results = json.load(f)
                except FileNotFoundError:
                    results = {}

                # pone de llave la hora
                key = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                results[key] = result

                with open(f'data_history/results_{symbol}_{interval_time}.json', 'w') as f:
                    json.dump(results, f, indent=4)

        # Espera n segundos antes del próximo ciclo
        mult = int(interval_time.replace("m", ""))
        time.sleep(time_seg*mult) ### falta hacer multiplicador por interval_time

