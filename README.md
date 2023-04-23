
# Cryptocurrency Perpetual Market Tracker Bot

This bot retrieves real-time data from the cryptocurrency perpetual market using the API from coinglass.com. The data is stored in a CSV file and can be used to track the performance of a specific cryptocurrency.

## How to run

Clone the repository to your local machine.

## Install the required dependencies by running the following command:

      pip install pandas requests
      
## Open the main.py file and edit the retrieve_data function with the desired symbol and frequency.

      retrieve_data("BTC", 6)
  
The retrieve_data function takes two parameters: symbol and frequency. The symbol parameter specifies the cryptocurrency to track and the frequency parameter specifies how often the data should be retrieved.


## Run the main.py file by typing the following command in the terminal:

      python main.py
  
 
The data is retrieved from the coinglass.com API and is stored in a pandas DataFrame. The necessary data is then extracted from the DataFrame and stored in a new DataFrame with the desired format. The data is then logged to a CSV file with the name "{symbol}_data.csv".
