### generate history data microservice

import json
from tradingview_ta import TA_Handler
from datetime import datetime




def create_data(num_data, time_seg, interval_time, financial_asset_info):
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

                # Carga los resultados existentes, añade el nuevo resultado y guarda
                try:
                    with open(f'data_history/results_{symbol}_{interval_time}.json', 'r') as f:
                        results = json.load(f)
                except FileNotFoundError:
                    results = {}
                except json.JSONDecodeError as e:
                    print(f"Error parsing JSON data: {e}")
                    results = {}

                # pone de llave la hora
                key = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                results[key] = result

                with open(f'data_history/results_{symbol}_{interval_time}.json', 'w') as f:
                    json.dump(results, f, indent=4)
