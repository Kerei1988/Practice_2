
import matplotlib.pyplot as plt
import pandas as pd

from data_download import  add_moving_average, rsi_func, macd_func


def create_and_save_plot(data: pd.DataFrame, ticker: str, period: str, filename: str=None) -> None:
    """
    Создаёт график, отображающий цены закрытия и скользящие средние.
    Предоставляет возможность сохранения графика в файл.
    Параметр filename опционален; если он не указан, имя файла генерируется автоматически.

    :param data: DataFrame, содержащий исторические данные акций с колонками 'Close' и 'Moving_Average'.
    :param ticker: Str тикер акции для заголовка графика.
    :param period: Str период времени для данных (например: '1mo', '2020-02-01/2021-02-01').
    :param filename: Str имя файла для сохранения графика; если не указано, имя генерируется автоматически.
    :return: None
    """
    dates = None
    data['RSI'] = rsi_func(data)
    macd_df = macd_func(data)
    data = data.join(macd_df)
    average = add_moving_average(data)
    pd.concat([data, average], join='inner', axis=1)

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")

    fig = plt.figure(figsize=(18, 12))
    gs = fig.add_gridspec(6, 1)

    ax1 = fig.add_subplot(gs[0:4, 0])
    ax1.plot(dates, data['Close'].values, label='Close Price', color='green')
    ax1.plot(dates, data['Moving_Average'].values, label='Moving Average', color='yellow')
    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    ax1.grid()
    ax1.legend()

    ax2 = fig.add_subplot(gs[4, 0])
    ax2.plot(dates, data['RSI'].values, label='RSI', color='blue')
    ax2.axhline(70, linestyle='--', alpha=1, color='red')
    ax2.axhline(30, linestyle='--', alpha=1, color='green')
    ax2.set_ylabel('RSI')
    ax2.grid()
    ax2.legend()

    ax3 = fig.add_subplot(gs[5, 0])
    ax3.plot(dates, data['MACD'].values, label='MACD', color='blue')
    ax3.plot(data.index, data['Signal'], label='Сигнальная линия', color='purple')
    ax3.set_ylabel('MACD')
    ax3.grid()
    ax3.legend()

    plt.tight_layout()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")







    # # Построение графиков
    # fig, ax1 = plt.subplots(figsize=(14, 8))  # Создание фигуры и одной оси
    #
    # # График цены закрытия
    # ax1.plot(data.index, data['Close'], label='Цена закрытия', color='blue')
    # ax1.set_ylabel('Цена (USD)', color='blue')
    # ax1.tick_params(axis='y', labelcolor='blue')
    #
    # # Создание второй оси для RSI
    # ax2 = ax1.twinx()  # Создание второй оси с общим x-значением
    # ax2.plot(data.index, data['RSI'], label='RSI', color='orange', alpha=0.5)
    # ax2.axhline(70, linestyle='--', alpha=0.5, color='red')  # Уровень перекупленности
    # ax2.axhline(30, linestyle='--', alpha=0.5, color='green')  # Уровень перепроданности
    # ax2.set_ylabel('RSI', color='orange')
    # ax2.tick_params(axis='y', labelcolor='orange')
    #
    # # Добавление MACD на тот же график с другой осью
    # ax3 = ax1.twinx()  # Создание третьей оси с общим x-значением
    # ax3.spines['right'].set_position(('outward', 60))  # Сдвиг третьей оси вправо
    # ax3.plot(data.index, data['MACD'], label='MACD', color='purple', alpha=0.5)
    # ax3.plot(data.index, data['Signal'], label='Сигнальная линия', color='red', alpha=0.5)
    # ax3.set_ylabel('MACD', color='purple')
    # ax3.tick_params(axis='y', labelcolor='purple')
    #
    # # Настройка графика
    # plt.title(f'График цены закрытия с RSI и MACD для {ticker}')
    # fig.tight_layout()  # Оптимизация расположения элементов
    #
    # # Показать график
    # plt.show()

    # fig, ax1 = plt.subplots()
    # ax1.set_xlabel('дата')
    # ax1.set_ylabel('цена закрытия')
    # ax1.plot(data.index, data['Close'], color='blue')
    #
    # ax2 = ax1.twinx()
    # ax2.set_ylabel('rsi')
    # ax2.plot(data.index, data['RSI'], label='RSI', color='orange', alpha=0.5)
    # ax2.axhline(70, linestyle='--', alpha=0.5, color='red')
    # ax2.axhline(30, linestyle='--', alpha=0.5, color='green')
    #
    # plt.title('Наложение графиков с различными показателями')
    # plt.grid(True)
    # plt.show()
    #
    # if filename is None:
    #     filename = f"{ticker}_{period}_stock_price_chart.png"
    # plt.savefig(filename)
    # print(f"График сохранен как {filename}")



    # fig, ax = plt.subplot(3, 1, figsize=(10, 8))
    #
    # ax.plot(data.index, data['Close'], label='Цена закрытия', color='blue')
    #
    # ax.plot(data.index, data['RSI'], label='RSI', color='orange', alpha=0.5)
    #
    # ax.plot(data.index, data['MACD'], label='MACD', color='purple', alpha=0.5)
    # ax.plot(data.index, data['Signal'], label='Сигнальная линия', color='red', alpha=0.5)
    #
    # plt.title(f'График цены закрытия с RSI и MACD для {ticker}')
    # plt.ylabel('Цена / Индикаторы')
    # plt.axhline(70, linestyle='--', alpha=0.5, color='red')
    # plt.axhline(30, linestyle='--', alpha=0.5, color='green')
    #
    # plt.grid()
    # plt.tight_layout()
    # plt.legend()
    #
    # if filename is None:
    #     filename = f"{ticker}_{period}_stock_price_chart.png"
    # plt.savefig(filename)
    # print(f"График сохранен как {filename}")




