
import pandas as pd


def calculate_and_display_average_price(data: pd.DataFrame, time_period: int = 3) -> pd.DataFrame:
    """
    Функция вычисляет и выводит среднюю цену закрытия акций за заданный период.

    :param data: DataFrame содержащий данные о ценах акций.
    Должен содержать колонку 'Close'.
    :param time_period: Количество периодов для расчета скользящей средней.
     По умолчанию равно 3.
    :return: DataFrame содержащий колонки 'Close' и 'Average_price'.
    """
    data['Average_price'] = data['Close'].rolling(window=time_period).mean()
    return data[['Close', 'Average_price']]