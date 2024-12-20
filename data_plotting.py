
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

from data_download import  add_moving_average, rsi_func, macd_func, standard_deviation


def create_and_save_plot(data: pd.DataFrame, ticker: str, period: str, fashion: str = 'classic',
                         filename: str=None, window: int = None) -> None:
    """
    Создаёт график, отображающий цены закрытия и скользящие средние.
    Предоставляет возможность сохранения графика в файл.
    Параметр filename опционален; если он не указан, имя файла генерируется автоматически.

    :param data: DataFrame, содержащий исторические данные акций с колонками 'Close' и 'Moving_Average'.
    :param ticker: Тикер акции для заголовка графика.
    :param period: Период времени для данных (например: '1mo', '2020-02-01/2021-02-01').
    :param filename: Имя файла для сохранения графика; если не указано, имя генерируется автоматически.
    :param fashion: Установка стиля графика. По умолчанию classic.
    :param window: Период за который нужно получить среднее отклонение
    :return: None
    """
    dates = None
    data['RSI'] = rsi_func(data)
    macd_df = macd_func(data)
    data = data.join(macd_df)
    average = add_moving_average(data)
    data = pd.concat([data, average], join='inner', axis=1)
    std_mean = standard_deviation(data, window=window)

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")

    fig = plt.figure(figsize=(18, 12))
    gs = fig.add_gridspec(6, 1)

    plt.style.use(fashion)

    ax1 = fig.add_subplot(gs[0:4, 0])
    ax1.plot(dates, data['Close'].values, label='Close Price', color='green')
    if window is not None:
        ax1.fill_between(dates,
                         std_mean['Mean'] - std_mean['STD'],
                         std_mean["Mean"] + std_mean['STD'], color="lightblue", alpha=0.5, label='Стандартное отклонение')
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




