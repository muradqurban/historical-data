import binance_data
import show

# Customize your data by adding files as needed
data_list = {
    1: './data/ETHUSDT-15m-2023-06.csv',
    2: './data/ETHUSDT-15m-2023-07.csv',
    3: './data/ETHUSDT-15m-2023-08.csv',
}

data = binance_data.readBinanceData(data_list)
data.to_csv('data.csv')
show.showCharts(data)