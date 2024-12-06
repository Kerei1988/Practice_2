
import data_download as dd
import data_plotting as dp

from task_1 import calculate_and_display_average_price as cada
from task_2 import notify_if_strong_fluctuations as nisf
from task_3 import export_data_to_csv as edtc


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    if 'Close' in stock_data.columns:
        # Writing the received data to a .csv file
        edtc(stock_data)

        # Price fluctuations with the specified threshold
        oscillation = nisf(stock_data, 4)

        # The average closing price of shares for a given period.
        average_price = cada(stock_data, time_period=7)
        print(average_price)

        # Add moving average to the data
        average = dd.add_moving_average(stock_data)
        print(average)

        # # Plot the data
        dp.create_and_save_plot(stock_data, ticker, period)
    else:
        raise ValueError(f"Отсутствует необходимый столбец: 'Close'")

if __name__ == "__main__":
    main()
