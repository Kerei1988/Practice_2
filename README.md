# Проект: Анализ Цен Акций

Этот проект предназначен для загрузки исторических данных об акциях и их визуализации.
Он использует библиотеку yfinance для получения данных и matplotlib для создания графиков.
Пользователи могут выбирать различные тикеры и временные периоды для анализа, а также просматривать движение цен и
скользящие средние на графике.

## Установка

Для работы с проектом вам потребуется Python и некоторые библиотеки (pandas, yfinance, matplotlib). 
Вы можете установить необходимые зависимости с помощью pip:

```bash
pip install pandas yfinance matplotlib

### Задание 1. Реализовать функцию calculate_and_display_average_price(data), которая вычисляет и выводит среднюю цену
      закрытия акций за заданный период.

      Функция будет принимать DataFrame и вычислять среднее значение колонки 'Close'. 
      Результат будет выводиться в консоль.
      
       def calculate_and_display_average_price(data, time_period=3):
            """
          Функция вычисляет и выводит среднюю цену закрытия акций за заданный период.
      
          :param data: DataFrame, содержащий данные о ценах акций. Должен содержать колонку 'Close'.
          :param time_period: int, количество периодов для расчета скользящей средней. По умолчанию равно 3.
          :return: DataFrame, содержащий колонки 'Close' и 'Average_price'.
          """
          data['Average_price'] = data['Close'].rolling(window=time_period).mean()
          return data[['Close', 'Average_price']]               

      # пример работы функции calculate_and_display_average_price

        import data_download as dd
        from task_1 import calculate_and_display_average_price as cda

            def main():
                print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
                print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), 
                       GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
                print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л,
                       с начала года, макс.")
            
                ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
                period = input("Введите период для данных (например, '1mo' для одного месяца): ")

                # Получает исторические данные об акциях для указанного тикера и временного периода. Возвращает DataFrame с данными.
                stock_data = dd.fetch_stock_data(ticker, period)

                # Функция вычисляет и выводит среднюю цену закрытия акций за заданный период
                avarage_price = cda(stock_data)

                # Выведет первые 8 строк
                print(avarage_price.head(8))  

        if __name__ == "__main__":
                main()


        # Результат работы функции
        ## Введненные данные: тикер - APPL, период - 1 месяц, средняя цена закрытия акций - 3 дня

                                              Close  Average_price
              Date                                                
              2024-11-04 00:00:00-05:00  221.766006            NaN
              2024-11-05 00:00:00-05:00  223.204422            NaN
              2024-11-06 00:00:00-05:00  222.475235     222.481888
              2024-11-07 00:00:00-05:00  227.229996     224.303218
              2024-11-08 00:00:00-05:00  226.960007     225.555079
              2024-11-11 00:00:00-05:00  224.229996     226.139999
              2024-11-12 00:00:00-05:00  224.229996     225.139999

        ## Введненные данные: тикер - MSFT, период - 1 месяц, средняя цена закрытия акций - 7 дней

                                              Close  Average_price
              Date                                                
              2024-11-04 00:00:00-05:00  407.644043            NaN
              2024-11-05 00:00:00-05:00  410.638031            NaN
              2024-11-06 00:00:00-05:00  419.340607            NaN
              2024-11-07 00:00:00-05:00  424.580139            NaN
              2024-11-08 00:00:00-05:00  421.695923            NaN
              2024-11-11 00:00:00-05:00  417.174957            NaN
              2024-11-12 00:00:00-05:00  422.184937     417.608377
              2024-11-13 00:00:00-05:00  424.350616     419.995030
              2024-11-14 00:00:00-05:00  426.037231     422.194916
              2024-11-15 00:00:00-05:00  414.170990     421.45639


### Задание 2.  Разработать функцию notify_if_strong_fluctuations(data, threshold), которая анализирует данные и 
            уведомляет пользователя, если цена акций колебалась более чем на заданный процент за период.

            # Функция будет вычислять максимальное и минимальное значения цены закрытия и сравнивать разницу с заданным
                порогом. Если разница превышает порог, пользователь получает уведомление.

            def notify_if_strong_fluctuations(data, threshold):
                """
                 Функция уведомляет о сильных колебаниях цен акций на основе заданного порога.
                 :param data: DataFrame, содержащий данные о ценах акций. Должен содержать колонку 'Close'.
                 :param threshold: float, пороговое значение для определения сильных колебаний.
                 :return: str или None. Возвращает сообщение о колебаниях, если они превышают порог; иначе None.
                 """
                len_data = len(data)
                if data.empty or 'Close' not in data.columns or len_data < 2:
                    return 'Нет данных для анализа'
                for i in range(1, len_data):
                    oscillation = abs(data.iloc[i]['Close'] - data.iloc[i - 1]['Close'])
                    percent_oscillation = (oscillation/data.iloc[i - 1]['Close'])*100
                    if percent_oscillation > threshold:
                        print(f'Дата: {data.index[i].strftime('%Y-%m-%d')},
                               Колебание цены = {percent_oscillation.round(2)}, больше указанного порога =                                     {threshold}')
                return None

       # пример работы функции calculate_and_display_average_price

        import data_download as dd
        from task_2 import notify_if_strong_fluctuations as nsf

            def main():
                print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
                print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc),
                      GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
                print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л,
                      с начала года, макс.")
            
                ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
                period = input("Введите период для данных (например, '1mo' для одного месяца): ")

                # Получает исторические данные об акциях для указанного тикера и временного периода. Возвращает DataFrame с данными.
                stock_data = dd.fetch_stock_data(ticker, period)

                # Функция вычисляет и выводит среднюю цену закрытия акций за заданный период
                oscillation_price = nsf(stock_data, 2)

                # Выведет первые 8 строк
                print(oscillation_price.)  

        if __name__ == "__main__":
                main()

      # Результат работы функции
            # тикер - AAPL, период - 1 месяц, указаный порог 2%
            Дата: 2024-11-07, Колебание цены = 2.14, больше указанного порога = 2

            # тикер - AAPL, период - 1 год , указаный порог 4%
            Дата: 2024-03-21, Колебание цены = 4.09, больше указанного порога = 4
            Дата: 2024-04-11, Колебание цены = 4.33, больше указанного порога = 4
            Дата: 2024-05-03, Колебание цены = 5.98, больше указанного порога = 4
            Дата: 2024-06-11, Колебание цены = 7.26, больше указанного порога = 4
            Дата: 2024-08-05, Колебание цены = 4.82, больше указанного порога = 4


### Задание 3.   Добавить функцию export_data_to_csv(data, filename), которая позволяет сохранять загруженные 
                 данные об акциях в CSV файл.

            def export_data_to_csv(data, filename=None):
                """
                Функция принимает DataFrame и имя файла, после чего сохранять данные в указанный файл.
                :param data: экземпляр pandas DataFrame или список словарей
                :param filename: Имя файла, по умолчанию создается имя файла в котором указана дата создания
                :return: создает файл в формате .csv
                """
                if filename is None:
                    filename = f"file_{datetime.now().strftime('%Y-%m-%d')}.csv"
                if isinstance(data, pd.DataFrame):
                    data.to_csv(filename, index=False, encoding='utf-8')
                else:
                    raise ValueError("data должно быть экземпляром pandas DataFrame или списком словарей")
            
                print(f"Данные успешно экспортированы в файл: {filename}")


    # пример работы функции
      import data_download as dd
      from task_3 import export_data_to_csv as edc

      def main():
          print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
          print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), 
          GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
          print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л,
                 с начала года, макс.")
      
          ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
          period = input("Введите период для данных (например, '1mo' для одного месяца): ")
      
          # Fetch stock data
          stock_data = dd.fetch_stock_data(ticker, period)
      
          edc(stock_data)

    # Введенные данные: тикер - AAPL, период- 1 месяц, имя файла создано по умолчанию
    # вывод в консоле:
      Добро пожаловать в инструмент получения и построения графиков биржевых данных.
      Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), 
      MSFT (Microsoft Corporation), AMZN             (Amazon.com Inc), TSLA (Tesla Inc).
      Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.
      Введите тикер акции (например, «AAPL» для Apple Inc):»AAPL
      Введите период для данных (например, '1mo' для одного месяца): 1mo
      Данные успешно экспортированы в файл: file_2024-12-04.csv
      
### Задание №4. Реализовать функционал: Добавление дополнительных технических индикаторов
     Реализовать функции для расчёта и отображения на графике дополнительных технических индикаторов,
     например, RSI или MACD.
    
    
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
    
    
    # Функции индикаторов MACD и RSI, реализованы в функции create_and_save_plot, 
      выводятся на одном грфике под основным.
      
    def create_and_save_plot(data: pd.DataFrame, ticker: str, period: str, filename: str=None) -> None:
        """
        Создаёт график, отображающий цены закрытия и скользящие средние.
        Предоставляет возможность сохранения графика в файл.
        Параметр filename опционален; если он не указан, имя файла генерируется автоматически.
    
        :param data: DataFrame, содержащий исторические данные акций с колонками 'Close' и 'Moving_Average'.
        :param ticker: Str тикер акции для заголовка графика.
        :param period: Str период времени для данных (например, '1mo').
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

    # Пример работы функций

    Добро пожаловать в инструмент получения и построения графиков биржевых данных.
    Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), 
    MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).
    Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.
    Введите тикер акции (например, «AAPL» для Apple Inc):»MSFT
    Введите период для данных (например, '1mo' для одного месяца): 1y
    Данные успешно экспортированы в файл: file_2024-12-06.csv
    

### Задача №5. Реализовать функционал: Улучшенное управление временными периодами.
    # Функция fetch_stock_data была доработана: прием двух параметров - дата начальная и дата конечная,
     для фильтрации данных; Так же обработка исключений, если пользователь вводит неверные данные
     
    def fetch_stock_data(ticker:str, start: str = None, end: str = None, period: str = '1mo',) -> pd.DataFrame:
    """
     Получает исторические данные об акциях для указанного тикера и временного периода.
     Возвращает DataFrame с данными.

    :param ticker: Обозначающая тикер акции (например, "AAPL" для Apple Inc.).
    :param start: Дата начала исторических данных.
    :param end: Дата конца исторических данных.
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
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period=period, start=start, end=end)
        return data
    except Exception as exc:
        print(f"{exc}")

    # main модифицирован для приема дополнительных данных(конкретные даты начала и окончания для анализа).
      Так же добавлены обработка исключений как при получении данных о тикере, так и при запросе исторических данных.
      Используются циклы while для повторного запроса ввода от пользователя в случае ошибки. 
        
        def main():
            period = None
            stock_data = pd.DataFrame
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
        
            while True:
                choices = input("Хотите ввести конкретные даты (введите 'Dates') или"
                                " выбрать предустановленный период (введите 'Period'): ").strip().lower()
                if choices == 'dates':
                    while True:
                        start_date = input("Введите начальную дату данных (в формате YYYY-MM-DD): ")
                        end_date = input("Введите конечную дату для анализа (в формате YYYY-MM-DD): ")
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
                    break
        
                else: print("Неверный ввод. Нужно ввести 'дата' или 'период'. Пожалуйста, начните заново(в формате YYYY-MM-DD).")
                break
                
    # Пример работы
        Добро пожаловать в инструмент получения и построения графиков биржевых данных.
        Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).
        Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.
        Введите тикер акции (например, «AAPL» для Apple Inc): AAPL
        Хотите ввести конкретные даты (введите 'Dates') или выбрать предустановленный период (введите 'Period'): dates
        Введите начальную дату данных (в формате YYYY-MM-DD): 2024-02-01
        Введите конечную дату для анализа (в формате YYYY-MM-DD): 2024-06-01
        
                                        Open        High  ...  Dividends  Stock Splits
        Date                                               ...                         
        2024-02-01 00:00:00-05:00  183.093032  186.038593  ...        0.0           0.0
        2024-02-02 00:00:00-05:00  178.983166  186.416750  ...        0.0           0.0
        2024-02-05 00:00:00-05:00  187.232740  188.327383  ...        0.0           0.0
        2024-02-06 00:00:00-05:00  185.949029  188.387082  ...        0.0           0.0
        2024-02-07 00:00:00-05:00  189.710602  190.118607  ...        0.0           0.0
        ...                               ...         ...  ...        ...           ...
        2024-05-24 00:00:00-04:00  188.394430  190.150457  ...        0.0           0.0
        2024-05-28 00:00:00-04:00  191.078346  192.564993  ...        0.0           0.0
        2024-05-29 00:00:00-04:00  189.182654  191.816704  ...        0.0           0.0
        2024-05-30 00:00:00-04:00  190.330052  191.746850  ...        0.0           0.0
        2024-05-31 00:00:00-04:00  191.008509  192.135967  ...        0.0           0.0
        
        [84 rows x 7 columns]
        Данные успешно экспортированы в файл: file_2024-12-08.csv
        Дата: 2024-03-21, Колебание цены = 4.09, больше указанного порога = 4
        Дата: 2024-04-11, Колебание цены = 4.33, больше указанного порога = 4
        Дата: 2024-05-03, Колебание цены = 5.98, больше указанного порога = 4
                                        Close  Average_price
        Date                                                
        2024-02-01 00:00:00-05:00  185.949036            NaN
        2024-02-02 00:00:00-05:00  184.943970            NaN
        2024-02-05 00:00:00-05:00  186.765030            NaN
        2024-02-06 00:00:00-05:00  188.377136            NaN
        2024-02-07 00:00:00-05:00  188.486603            NaN
        ...                               ...            ...
        2024-05-24 00:00:00-04:00  189.551804     189.694342
        2024-05-28 00:00:00-04:00  189.561783     189.715722
        2024-05-29 00:00:00-04:00  189.861115     189.775589
        2024-05-30 00:00:00-04:00  190.858856     189.811223
        2024-05-31 00:00:00-04:00  191.816681     189.796967
        
        [84 rows x 2 columns]
                                   Moving_Average
        Date                                     
        2024-02-01 00:00:00-05:00             NaN
        2024-02-02 00:00:00-05:00             NaN
        2024-02-05 00:00:00-05:00             NaN
        2024-02-06 00:00:00-05:00             NaN
        2024-02-07 00:00:00-05:00      186.904355
        ...                                   ...
        2024-05-24 00:00:00-04:00      189.801245
        2024-05-28 00:00:00-04:00      189.591718
        2024-05-29 00:00:00-04:00      189.180646
        2024-05-30 00:00:00-04:00      189.258472
        2024-05-31 00:00:00-04:00      190.330048
        
        [84 rows x 1 columns]
        График сохранен как AAPL_2024-02-01:2024-06-01_stock_price_chart.png