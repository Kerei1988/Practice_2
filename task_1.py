
def calculate_and_display_average_price(data, time_period=3):
    """
    Функция вычисляет и выводит среднюю цену закрытия акций за заданный период.

    :param data: DataFrame, содержащий данные о ценах акций. Должен содержать колонку 'Close'.
    :param time_period: int, количество периодов для расчета скользящей средней. По умолчанию равно 3.
    :return: DataFrame, содержащий колонки 'Close' и 'Average_price'.
    """
    data['Average_price'] = data['Close'].rolling(window=time_period).mean()
    return data[['Close', 'Average_price']]