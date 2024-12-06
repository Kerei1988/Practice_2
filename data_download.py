import pandas as pd
import yfinance as yf


def fetch_stock_data(ticker:str, period: str = '1mo') -> pd.DataFrame:
    """
     Получает исторические данные об акциях для указанного тикера и временного периода.
     Возвращает DataFrame с данными.

    :param ticker: Обозначающая тикер акции (например, "AAPL" для Apple Inc.).
    :param period: Временной диапазон, за который вы хотите получить данные.
    По умолчанию 14.
    Он может принимать значения, такие как:
    '1d': 1 день
    '5d': 5 дней
    '1mo': 1 месяц
    '3mo': 3 месяца
    '6mo': 6 месяцев
    '1y': 1 год
    '2y': 2 года
    '5y': 5 лет
    '10y': 10 лет
    'ytd': с начала года
    'max': максимальный доступный период
    :return: DataFrame возвращает отфильтрованные данные по указанным параметрам
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data

def add_moving_average(data: pd.DataFrame, window_size: int = 5) -> pd.DataFrame:
    """
    Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия.

    :param data: DataFrame с историческими данными акций, должен содержать колонку 'Close'.
    :param window_size: Размер окна для расчета скользящего среднего (по умолчанию 5).
    :return: Обновленный DataFrame с добавленной колонкой 'Moving_Average'.
    """
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data[['Moving_Average' ]]

def rsi_func(data: pd.DataFrame, period: int = 14) -> pd.DataFrame:
    """
        Рассчитывает индекс относительной силы (RSI) для заданного DataFrame.

        :param data: DataFrame с историческими данными акций, должен содержать колонку 'Close'.
        :param period: Период для расчета RSI (по умолчанию 14).
        :return: Значение RSI на последней дате.
        """
    data['Price changes'] = data['Close'].diff()

    data["positive change"] = data["Price changes"].clip(lower=0)
    data["negative change"] = -data["Price changes"].clip(upper=0)

    ewma_pos_change = data["positive change"].ewm(com=period - 1, adjust=False).mean()
    ewma_neg_change = data["negative change"].ewm(com=period - 1, adjust=False).mean()

    rs = ewma_pos_change / ewma_neg_change
    rsi= 100 - (100/(1 + rs))
    return rsi

def macd_func(data: pd.DataFrame, short_period: int = 12, long_period: int = 26, signal_period: int = 9) -> pd.DataFrame:
    """
    Функция рассчитывает технический индикатор (MACD) и сигнальную линию для заданного DataFrame.

    :param data: DataFrame с историческими данными акций, должен содержать колонку 'Close'.
    :param short_period: Период для короткой EMA (по умолчанию 12).
    :param long_period: Период для длинной EMA (по умолчанию 26).
    :param signal_period: Период для сигнальной линии EMA (по умолчанию 9).
    :return: DataFrame[['MACD', 'Signal']]
    """
    short_ewma = data['Close'].ewm(com=short_period, adjust=False).mean()
    long_ewma = data['Close'].ewm(com=long_period, adjust=False).mean()
    macd = short_ewma - long_ewma

    signal = macd.ewm(com=signal_period, adjust=False).mean()
    return pd.DataFrame({'MACD': macd, 'Signal': signal})
