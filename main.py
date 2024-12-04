
import data_download as dd
import data_plotting as dplt
from task_1 import calculate_and_display_average_price as cda
from task_2 import notify_if_strong_fluctuations as nsf
from task_3 import export_data_to_csv as edc

def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # Writing the received data to a .csv file
    edc(stock_data)

    # Price fluctuations with the specified threshold
    oscillation = nsf(stock_data, 4)

    # The average closing price of shares for a given period.
    avarage_price = cda(stock_data, time_period=7)
    print(avarage_price.head(10))

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)


if __name__ == "__main__":
    main()
