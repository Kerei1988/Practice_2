
import yfinance as yf

def fetch_stock_data(ticker:str, period='1mo'):
    """
     Получает исторические данные об акциях для указанного тикера и временного периода.
     Возвращает DataFrame с данными.

    :param ticker: Str обозначающая тикер акции (например, "AAPL" для Apple Inc.).
    :param period: Str Временной диапазон, за который вы хотите получить данные.
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

def add_moving_average(data, window_size=5):
    """
    Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия.

    :param data: DataFrame с историческими данными акций, должен содержать колонку 'Close'.
    :param window_size: Int Размер окна для расчета скользящего среднего (по умолчанию 5).
    :return: Обновленный DataFrame с добавленной колонкой 'Moving_Average'.
    """
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data
