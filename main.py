import requests
import pandas as pd
from datetime import datetime
import time

def retrieve_data(symbol, frequency):
    url = f"https://open-api.coinglass.com/public/v2/perpetual_market?symbol={symbol}"
    headers = {
        "accept": "application/json",
        "coinglassSecret": "<YOUR-SECRET-KEY>"
    }

    while True:
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()["data"][symbol]
                df = pd.DataFrame(data, columns=[
                    "exchangeName",
                    "price",
                    "updateTime",
                    "shortVolUsd",
                    "longVolUsd",
                    "buyTurnoverNumber",
                    "sellTurnoverNumber",
                ])
                # Sum up values from all exchanges
                price = df["price"].mean()
                buy_turnover_number = df["buyTurnoverNumber"].sum()
                sell_turnover_number = df["sellTurnoverNumber"].sum()
                short_vol_usd = df["shortVolUsd"].sum()
                long_vol_usd = df["longVolUsd"].sum()
                # Convert updateTime to readable date and time
                update_time = datetime.fromtimestamp(df["updateTime"].iloc[0]/1000)
                # Store necessary data in a new DataFrame
                df = pd.DataFrame({
                    "Price": price,
                    "Symbol": symbol,
                    "shortVolUsd": short_vol_usd,
                    "longVolUsd": long_vol_usd,
                    "buyTurnoverNumber": buy_turnover_number,
                    "sellTurnoverNumber": sell_turnover_number,
                    "NetVolUsd": long_vol_usd - short_vol_usd,
                    "NetTurnoverNumber": buy_turnover_number - sell_turnover_number,
                    "NetPosition": (long_vol_usd - short_vol_usd) / price,
                    "UpdateTime": update_time
                }, index=[0])
                print(df)
                # Log the data to a CSV file
                filename = f"{symbol}_data.csv"
                df.to_csv(filename, mode="a", header=False)
        except Exception as e:
            print(f"An error has occurred: {e}. Restarting the function...")
        time.sleep(frequency)


if __name__ == "__main__":
    retrieve_data("BTC", 6)
