
def notify_if_strong_fluctuations(data, threshold):
    """
     Функция уведомляет о сильных колебаниях цен акций на основе заданного порога.

     :param data: DataFrame, содержащий данные о ценах акций. Должен содержать колонку 'Close'.
     :param threshold: Float, пороговое значение для определения сильных колебаний.
     :return: Str или None. Возвращает сообщение о колебаниях, если они превышают порог;
     иначе None.
     """
    len_data = len(data)
    if data.empty or 'Close' not in data.columns or len_data < 2:
        return 'Нет данных для анализа'
    for i in range(1, len_data):
        oscillation = abs(data.iloc[i]['Close'] - data.iloc[i - 1]['Close'])
        percent_oscillation = (oscillation / data.iloc[i - 1]['Close'])*100
        if percent_oscillation > threshold:
            print(f'Дата: {data.index[i].strftime('%Y-%m-%d')}, '
                  f'Колебание цены = {percent_oscillation.round(2)}, '
                  f'больше указанного порога = {threshold}')
    return None