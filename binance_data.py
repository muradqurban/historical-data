import pandas as pd


def readBinanceData (data_list):
    data = pd.DataFrame(columns=['date', 'open', 'high', 'low', 'close', 'volume', 'close_time'])

    for i in range(1, len(data_list)+1):
        new_data = pd.read_csv(data_list[i])

        # Drop unnecessary columns
        new_data = new_data.drop(columns=['quote_volume', 'count', 'taker_buy_volume', 'taker_buy_quote_volume', 'ignore'])

        # Rename columns
        new_data.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'close_time']

        # Convert timestamps to datetime objects
        new_data['date'] = pd.to_datetime(new_data['date'], unit='ms')
        new_data['close_time'] = pd.to_datetime(new_data['close_time'], unit='ms')

        # Display missing values
        missing_values = new_data.isnull().sum()
        missing_values = missing_values[missing_values > 0]
        print("Missing values:")
        print(missing_values)

        # Sort data by date
        new_data = new_data.sort_values(by='date')

        # Reset index
        new_data = new_data.reset_index(drop=True)
        data = pd.concat([data, new_data], ignore_index=True)
    return data

