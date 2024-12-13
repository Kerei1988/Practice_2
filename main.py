from pprint import pprint

import pandas as pd
import yfinance as yf

import data_download as dd
import data_plotting as dp

from task_1 import calculate_and_display_average_price as cada
from task_2 import notify_if_strong_fluctuations as nisf
from task_3 import export_data_to_csv as edtc


def main():
    chart_style = ['Solarize_Light2', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot',
                   'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark',
                   'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted',
                   'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster',
                   'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid',
                   'tableau-colorblind10']
    style = ""
    period = None
    stock_data = pd.DataFrame
    std = 20
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), "
          "GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л,"
          " с начала года, макс.")

    while True:
        ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc): ")

        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            if 'symbol' not in info or info['symbol'] != ticker:
                raise ValueError("Некорректный тикер.")
            break
        except Exception as e:
            print(f"Ошибка: {e}. Пожалуйста, проверьте введённый тикер.")

    option_style = input('Хотите выбрать стиль для графика введите "Yes", иначе "No": ').strip().lower()
    if option_style == 'yes':
        while True:
            print("Стили отображения графика:", ',\n '.join(chart_style))
            style = input(f"Введите название желаемого стиля: ")
            if style in chart_style:
                break
            print('Введите название стиля из списка!')
    if option_style == 'no':
        style = 'classic'

    while True:
        try:
            enter_std = (input('Установите период для вычисления среднего отклонения(по умолчанию равно 20 дней - нажмите Enter): '))
            if enter_std == '':
                break
            else:
                std = int(enter_std)
                break
        except ValueError:
            print('Введите целое число!')

    while True:
        choices = input("Хотите ввести конкретные даты (введите 'Dates') или"
                        " выбрать предустановленный период (введите 'Period'): ").strip().lower()
        if choices == 'dates':
            while True:
                start_date = input("Введите начальную дату данных (в формате YYYY-MM-DD): ")
                end_date = input("Введите конечную дату для анализа (в формате YYYY-MM-DD): ")
                period = f'{start_date}:{end_date}'
                try:
                    stock_data = dd.fetch_stock_data(ticker, start=start_date, end=end_date)
                    if stock_data.empty:
                        raise ValueError("Введенные данные не корректны.")
                    break
                except Exception as exc:
                    print(f"Ошибка при получении данных: {exc}. Пожалуйста, попробуйте снова.")
            break

        elif choices == 'period':
            while True:
                period = input("Введите период для данных (например, '1mo' для одного месяца): ")
                try:
                    stock_data = dd.fetch_stock_data(ticker, period=period)
                    if stock_data.empty:
                        raise ValueError("Введенные данные не корректны.")
                    break
                except Exception as exc:
                    print(f"Ошибка при получении данных: {exc}. Пожалуйста, попробуйте снова.")

        else: print("Неверный ввод. Нужно ввести 'дата' или 'период'. Пожалуйста, начните заново(в формате YYYY-MM-DD).")
        break

    if 'Close' in stock_data.columns and not stock_data.empty:

        # Writing the received data to a .csv file
        # edtc(stock_data)

        # Price fluctuations with the specified threshold
        # oscillation = nisf(stock_data, 4)

        # The average closing price of shares for a given period.
        # average_price = cada(stock_data, time_period=7)
        # print(average_price)

        # Add moving average to the data
        # average = dd.add_moving_average(stock_data)
        # print(average)

        # # Plot the data
        dp.create_and_save_plot(stock_data, ticker, period, fashion=style, window=std)

    else:
        raise ValueError(f"Отсутствует необходимый столбец: 'Close'")

if __name__ == "__main__":
    main()
