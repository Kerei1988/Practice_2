
import pandas as pd
from datetime import datetime

def export_data_to_csv(data, filename=None):
    """
    Функция принимает DataFrame и имя файла, после чего сохранять данные в указанный файл.

    :param data: Экземпляр pandas DataFrame или список словарей
    :param filename: Str Имя файла, по умолчанию создается имя файла в котором указана
     дата создания
    :return: None
    """
    if filename is None:
        filename = f"file_{datetime.now().strftime('%Y-%m-%d')}.csv"
    if isinstance(data, pd.DataFrame):
        data.to_csv(filename, index=False, encoding='utf-8')
    else:
        raise ValueError("data должно быть экземпляром pandas DataFrame или списком словарей")
    print(f"Данные успешно экспортированы в файл: {filename}")