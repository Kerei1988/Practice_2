
def calculate_and_display_average_price(data, time_period=3):
    """
    Функция вычисляет и выводит среднюю цену закрытия акций за заданный период.

    :param data: DataFrame
    :param time_period: int
    :return: DataFrame
    """
    data['Average_price'] = data['Price'].rolling(window=time_period).mean()
    return data[['Price', 'Average_price']]