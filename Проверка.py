
# Модуль 1: Установка нужных библиотек через терминал:

    # Откройте терминал и последовательно введите данные комманды
    # pip install numpy
    # pip install matplotlib
    # pip install mplcursors



# Модуль 2: Подключение библиотек для построения кода

        # Подключение библиотеки numpy
import numpy as np                              # Импортирует модуль numpy и присваевает ему псевдоним np (Модуль преднозначен для введения математических функций)
        # Подключение библиотеки matplotlib
import matplotlib.pyplot as plt                 # Импортирует подмодуль pyplot из модуля matplotlib и присваевает ему псевдоним plt (Подмодуль преднозначен для визализации 
                                                #   данных при помощи графиков и их построения)
        # Подключение библиотеки math
import math                                     # Импортирует модуль math



# Модуль 3: Ввод данных и их проверка

# Подмодуль 3.1: Функции для ввода правильных данных 

def input_elements(prompt):
    """
    Функция для запроса у пользователя названий элементов, разделенных запятыми.
        Параметры:
    prompt (str): Сообщение для запроса ввода.
        Возвращает:
    list: Список названий элементов.
    """
    while True:                                                         # Бесконесный цикл, закончится когда будет удовлетворять условиям цикла
        try:                                                            # Блок try в котором будет запущен код
            data = input(prompt).split(',')                             # Запрашиваем ввод и разделяем строки по запятым
            data = [el.strip() for el in data if el.strip()]            # Удаляем лишние пробелы и пустые строки через списковое включение (list comprehension)
            if not data:                                                # Проверяем, что список не пустой. 
                raise ValueError("Список не может быть пустым.")        # Генерирует исключение через команду raise и даёт ему имя ValueError(), если список пуст
            return data                                                 # Возвращаем список элементов если список имеет хоть одно значение
        except ValueError as e:                                         # Блок Except в котором исключению дают псевдоним e. Работает если в блке try произошла генерация исключения.
            print(f"Ошибка: {e}. Попробуйте снова.")                    # Выводим сообщение об ошибке и запрашиваем ввод снова


def input_positive_floats(prompt, count):
    """
    Функция для запроса у пользователя списка положительных чисел с плавающей точкой.
        Параметры:
    prompt (str): Сообщение для запроса ввода.
    count (int): Ожидаемое количество значений.
        Возвращает:
    list: Список положительных чисел с плавающей точкой.
    """
    while True:
        try:
            data = list(map(float, input(prompt).split(',')))                                           # Преобразуем ввод в список (list()) чисел с плавающей точкой (map(float,))
            if len(data) != count:                                                                      # Проверяем количество введенных значений
                raise ValueError(f"Должно быть введено {count} значений.")
            if any(x < 0 and x != float('inf') for x in data):                                          # Проверяем, что все значения положительные или бесконечные any() - функция
                                                                                                        #   возвращает значение True, если хоть один элемент является истинным,
                                                                                                        #   возращает False, если все значения ложны.
                raise ValueError("Все значения должны быть положительными числами или бесконечными.")   # Если условие True
            return data                                                                                 # Если условие False
        except ValueError as e:
            print(f"Ошибка: {e}. Попробуйте снова.")                                                    


def input_non_negative_integers(prompt, count):
    """
    Функция для запроса у пользователя списка неотрицательных целых чисел.
        Параметры:
    prompt (str): Сообщение для запроса ввода.
    count (int): Ожидаемое количество значений.
        Возвращает:
    list: Список неотрицательных целых чисел.
    """
    while True:
        try:
            data = list(map(int, input(prompt).split(',')))                                         # Преобразуем ввод в список целых чисел
            if len(data) != count:                                                                  # Проверяем количество введенных значений
                raise ValueError(f"Должно быть введено {count} значений.")
            if any(x < 0 for x in data):                                                            # Проверяем, что все значения неотрицательные
                raise ValueError("Все значения должны быть неотрицательными целыми числами.")
            return data                                                                             # Возвращаем список значений
        except ValueError as e:
            print(f"Ошибка: {e}. Попробуйте снова.")                                                # Выводим сообщение об ошибке и запрашиваем ввод снова


def input_positive_float(prompt):
    """
    Функция для запроса у пользователя положительного числа с плавающей точкой.
        Параметры:
    prompt (str): Сообщение для запроса ввода.
        Возвращает:
    float: Положительное число с плавающей точкой.
    """
    while True:
        try:
            data = float(input(prompt))                                                             # Преобразуем ввод в число с плавающей точкой
            if data <= 0 and data == float('inf'):                                                  # Проверяем, что значение положительное но не бесконечное
                raise ValueError("Значение должно быть положительным числом или бесконечным.")
            return data                                                                             # Возвращаем значение
        except ValueError as e:
            print(f"Ошибка: {e}. Попробуйте снова.")                                                # Выводим сообщение об ошибке и запрашиваем ввод снова


# Подмодуль 3.2: Функции для создание и фильтрации словаря

def create_element_dict(names, half_lives, initial_amounts):
    """
    Функция для создания словаря элементов с их параметрами.
    Параметры:
    names (list): Список названий элементов.
    half_lives (list): Список периодов полураспада для каждого элемента.
    initial_amounts (list): Список начальных количеств ядер для каждого элемента.
    Возвращает:
    dict: Словарь элементов с параметрами 'half_life' и 'initial_amount'.
    """
    element_dict = {}                                                       # Создаем пустой словарь для хранения элементов
    for i in range(len(names)):                                             # Проходим по всем элементам в списке names, через условие для i в диапазоне длины списка range(len(names))
        element_dict[names[i]] = {                                          # Для каждого ключа в словаре создаётся вложенный словарь 
            'half_life': half_lives[i],                                     # Добавляем период полураспада (значение) с названием 'half_life'
            'initial_amount': initial_amounts[i]                            # Добавляем начальное количество ядер (значение) с названием 'initial_amount'
        }
    return element_dict                                                     # Возвращаем заполненный словарь

def filter_elements(element_dict):
    """
    Функция для фильтрации элементов, учитывая их периоды полураспада.
    Параметры:
    element_dict (dict): Словарь элементов с их параметрами.
    Возвращает:
    dict: Отфильтрованный словарь элементов.
    """
    filtered_dict = {}                                                              # Создаем пустой словарь для хранения отфильтрованных элементов
    last_amount = 0                                                                 # Переменная для хранения количества ядер от элементов с нулевым периодом полураспада
    for el, params in element_dict.items():                                         # Проходим по всем элементам словаря, где приписка .items() возвращает пары: 
                                                                                    #   ключ (el), значение (params).
        half_life = params['half_life']                                             # Присваевает переменной half_life значение из вложенного списка под названием 'half_life'
        if half_life == 0:                                                          # Если период полураспада равен 0
            last_amount += params['initial_amount']                                 # Добавляем количество ядер к last_amount из вложенного списка под названием 'initial_amount'
        else:                                                                       # Условие если период полураспада больше 0 или равен бесконечности
            if half_life != float('inf'):                                           # Если период полураспада конечен
                filtered_dict[el] = {                                               # В словарь filtered_dict для каждого ключа создаётся вложенный словарь
                    'half_life': half_life,                                         
                    'initial_amount': last_amount + params['initial_amount'],       # Добавляем начальное количество ядер плюс накопленное количество ядер от элементов  мгновенным 
                                                                                    #   типом распада (значение) с названием 'initial_amount'
                }
                last_amount = 0                                                     # Сбрасываем last_amount после добавления в словарь
            else:                                                                   # Если элемент стабильный (период полураспада равен бесконечности)
                filtered_dict[el] = {
                    'half_life': half_life,                                         
                    'initial_amount': last_amount + params['initial_amount'], 
                }
                last_amount = 0                                                     
    return filtered_dict                                                            # Возвращаем отфильтрованный словарь


# Подмодуль 3.3: Ввод данных

# Получение данных от пользователя:

# Создаёт переменную element_names и присваивает ей проверенный через функцию input_elements список названий элементов, которые мы ввели
element_names = input_elements("Введите названия элементов (через запятую): ")

# Создаёт переменную half_lives и присваевает ей проверенный через функцию input_positive_floats список периодов полураспада, которые мы ввели
half_lives = input_positive_floats("Введите периоды полураспада (через запятую): ", len(element_names))

# Создаёт переменную initial_amounts и присваевает ей проверенный через функцию input_non_negative_integers список начального количество ядер, которые мы ввели
initial_amounts = input_non_negative_integers("Введите начальные количества ядер (через запятую): ", len(element_names))

# Создаёт переменную time_experiment и присваивает ей проверенное через функцию input_positive_float значение, которое мы ввели
time_experiment = input_positive_float("Введите время эксперимента (в годах): ")

# Создаёт переменную time_step и присваивает ей проверенное через функцию input_positive_float значение, которое мы ввели
time_step = input_positive_float("Введите шаг (в годах): ")

# Создание словаря элементов через функцию create_element_dict, и присваивание его переменной element_dict
element_dict = create_element_dict(element_names, half_lives, initial_amounts)

# Фильтрация словаря через функцию filter_elements, и присваивание его переменной filtered_dict
filtered_dict = filter_elements(element_dict)
# Данные операции были проведены для упрощения и корректной работы программы. Все последующие функции и операции расчитаны для отфильтрованного словаря элементов.



# Модуль 4: Рассчёт данных методом Эйлера 

# Подмодуль 4.1: Функции для рассчёта системы дифференциальных уравнения матодом Эйлера

def calculate_decay_constants(filtered_dict):
    """
    Функция для расчета констант распада для каждого элемента.
    Параметры:
    filtered_dict (dict): Словарь элементов с их параметрами.
    Возвращает:
    dict: Словарь с константами распада для каждого элемента.
    """
    decay_constants = {}                                        # Создаем пустой словарь для хранения констант распада
    for element, params in filtered_dict.items():               
        half_life = params['half_life']                         
        if half_life == float('inf'):                           # Если элемент стабильный (период полураспада равен бесконечности)
            decay_constants[element] = 0                        # Константа распада равна 0
        else:                                                   # Если элемент имеет реальное значение периода распада
            decay_constants[element] = np.log(2) / half_life    # Рассчитываем константу распада по формуле
    return decay_constants                                      # Возвращаем словарь с константами распада, где ключ название элемента, а значение это константа распада.
                                                                #   Возвращать словарь decay_constants нужно для следующего этапа

def euler_method_divided(filtered_dict, time_experiment, time_step):
    """
    Функция для расчета распада элементов методом Эйлера.
    Параметры:
    filtered_dict (dict): Словарь элементов с их параметрами.
    time_experiment (float): Общее время эксперимента.
    time_step (float): Шаг времени для метода Эйлера.
    Возвращает:
    dict: Словарь с массивами количества ядер для каждого элемента на каждом шаге времени.
    """
    decay_constants = calculate_decay_constants(filtered_dict)                                      # Присваиваем словарю имя decay_constants, рассчитываем и заносим значения 
                                                                                                    #   через функцию calculate_decay_constants
    elements = list(filtered_dict.keys())                                                           # Присваиваем списку названий элементов, через возвращение ключей словаря (.keys()),
                                                                                                    #   и через команду list(), имя elements
    num_elements = len(elements)                                                                    # Количество элементов равно длине списка элементов
    num_steps = math.ceil(time_experiment / time_step) + 1                                          # Количество шагов времени. Считается через округление времени эксперимента 
                                                                                                    #   делённого на шаг времени плюс один. Лишний шаг нужен для начальных значений.
    element_arrays = {el: np.zeros(num_steps) for el in elements}                                   # Создаем словарь, где массивы для хранения количества ядер на каждом шаге
                                                                                                    #   являются значениями с ключами. Массивы состоят из нулей (np.zeros())
                                                                                                    #   с количеством ячеек num_steps 
    for el in elements:                                                     # Инициализируем начальное количество ядер.
        element_arrays[el][0] = filtered_dict[el]['initial_amount']         # Присваивает первой ячейке каждого массива из словаря массивов начальное значение ядер из 
                                                                            #   фильтрованного словаря параметров соответсвенно каждому элементу
    for i in range(num_steps - 1):                                                  # Проходим по каждому шагу времени. Шагов на один меньше, так как посчитанные значения будут
                                                                                    #   присваиваться массивам, первая ячейка уже занята начальными значениями.
        current_values = {el: element_arrays[el][i] for el in elements}             # Создаём словарь, где значения каждого ключа это значение из массива element_arrays на позиции i
        first_element = elements[0]                                                 # Присваивает переменной first_element первый элемент из списка elements
        rates = {first_element: -decay_constants[first_element] * current_values[first_element]}        # Создаём словарь для скоростей распада.
                                                                                                        #   Рассчитываем скорость изменения для первого элемента.
        for j in range(1, num_elements - 1):                                # Проходим по всем элементам, кроме первого и последнего
            el = elements[j]                                                # Присваивает переменной el j-ый элемент из списка elements
            prev_element = elements[j - 1]                                  # Присваивает переменной prev_element (j-1)-ый элемент из списка elements
            
            rates[el] = decay_constants[prev_element] * current_values[prev_element] - decay_constants[el] * current_values[el]  # Рассчитываем скорость изменения для текущего элемента.
                                                                                                                                 # Сохраняет скорось распада под ключом в словарь.
        last_element = elements[-1]                                                         # Присваевает переменной last_element последний элкмкнт из списка elements
        rates[last_element] = decay_constants[elements[-2]] * current_values[elements[-2]]  # Рассчитываем скорость изменения для последнего элемента
        
        for el in elements:                                                                         # Обновляем количество ядер для всех элементов на следующем шаге
            element_arrays[el][i + 1] = current_values[el] + time_step * rates.get(el, 0)           
                        # element_arrays[el][i + 1] — это количество ядер элемента el на следующем временном шаге (шаг i + 1) в массиве element_arrays.
                        # current_values[el] — текущее количество ядер элемента el на текущем шаге i.
                        # time_step — временной шаг, на который происходит переход.
                        # rates.get(el, 0) — скорость изменения количества ядер элемента el. Метод .get(el, 0) используется для получения значения из словаря rates с ключом el.
    
    return element_arrays       # Возвращаем словарь с массивами количества ядер для каждого элемента


# Подмодуль 4.2: Решение методом Эйлера

element_arrays_whole = euler_method_divided(filtered_dict, time_experiment, time_step)      # Присваивает переменной element_arrays_whole словарь где значения это массивы данных.
    # Подготовка данных для графиков
num_steps = math.ceil(time_experiment / time_step) + 1                                      # Присваиввает переменной num_steps значение округленных шагов плюс один
times = np.arange(0, num_steps * time_step, time_step)                                      # Присваивает переменной times массив где начало это 0, конец num_steps * time_step, 
                                                                                            #   и где в каждой ячейке значение на time_step больше чем в предыдущей
current_amounts = {el: element_arrays_whole[el] for el in filtered_dict}                    # Присваивает переменной current_amount словарь где ключ жто название элемента,
                                                                                            #   а значение это массивы просчитанных данных. Данный шаг нуден для вывода значений и ключей.



# Модуль 5: Отображение графиков 

# Подмодуль 5.1: Функции для отображения графиков

def find_maxima(y, t):
    """
    Функция для нахождения максимумов в данных.
    Параметры:
    y (list): Список значений (количество атомов).
    t (list): Список времени.
    Возвращает:
    list: Список кортежей (время, значение) для всех максимумов.
    """
    maxima = []                                         # Создаем пустой список для хранения максимумов
    for i in range(1, len(y) - 1):                      # Проходим по всем значениям, кроме первого и последнего
        if y[i - 1] < y[i] > y[i + 1]:                  # Проверяем условие максимума
            maxima.append((t[i], y[i]))                 # Добавляем максимум в список
    return maxima                                       # Возвращаем список максимумов

def plot_graph(ax, x, y, label, title, color='blue'):
    """
    Функция для отображения графика одного элемента.
    Параметры:
    ax (matplotlib.axes.Axes): Ось для построения графика.
    x (list): Список значений времени.
    y (list): Список значений количества атомов.
    label (str): Метка для графика.
    title (str): Заголовок графика.
    color (str, optional): Цвет графика. По умолчанию 'blue'.
    """
    ax.clear()                                              # Очищаем ось перед построением графика
    ax.plot(x, y, label=label, color=color)                 # Строим график
    ax.set_xlabel('Время (годы)')                           # Устанавливаем метку оси X
    ax.set_ylabel('Количество атомов')                      # Устанавливаем метку оси Y
    ax.set_title(title)                                     # Устанавливаем заголовок графика
    ax.legend()                                             # Добавляем легенду
    ax.axhline(np.mean(y), color='r', linestyle='--', label='Среднее значение')     # Добавляем горизонтальную линию среднего значения
    ax.legend()                                             # Обновляем легенду
    maxima = find_maxima(y, x)                              # Находим максимумы
    for t, value in maxima:                                 # Проходим по всем максимумам
        ax.plot(t, value, 'ro')                             # Отображаем максимумы красными точками
    plt.draw()                                              # Обновляем график

def plot_combined_graph(ax, x, y_dict, title):
    """
    Функция для отображения объединенного графика для всех элементов.
    Параметры:
    ax (matplotlib.axes.Axes): Ось для построения графика.
    x (list): Список значений времени.
    y_dict (dict): Словарь с данными для каждого элемента (значения и цвет).
    title (str): Заголовок графика.
    """
    ax.clear()                                              # Очищаем ось перед построением графика
    for label, (y, color) in y_dict.items():                # Проходим по всем элементам в словаре
        ax.plot(x, y, label=label, color=color)             # Строим график для каждого элемента
    ax.set_xlabel('Время (годы)')                           # Устанавливаем метку оси X
    ax.set_ylabel('Количество атомов')                      # Устанавливаем метку оси Y
    ax.set_title(title)                                     # Устанавливаем заголовок графика
    ax.legend()                                             # Добавляем легенду
    plt.draw()                                              # Обновляем график

def create_single_element_plot(ax, times, current_amounts, element, color):
    """
    Функция для создания графика одного элемента.
    Параметры:
    ax (matplotlib.axes.Axes): Ось для построения графика.
    times (list): Список значений времени.
    current_amounts (dict): Словарь с количеством атомов для каждого элемента.
    element (str): Название элемента для построения графика.
    color (str): Цвет графика.
    """
    title = f'Изменение количества атомов {element}'                                # Формируем заголовок графика
    plot_graph(ax, times, current_amounts[element], element, title, color)          # Строим график для одного элемента

def create_combined_plot(ax, times, current_amounts, colors, element_names):
    """
    Функция для создания объединенного графика для всех элементов.
    Параметры:
    ax (matplotlib.axes.Axes): Ось для построения графика.
    times (list): Список значений времени.
    current_amounts (dict): Словарь с количеством атомов для каждого элемента.
    colors (list): Список цветов для каждого элемента.
    element_names (list): Список названий элементов.
    """
    y_dict = {element: (current_amounts[element], color) for element, color in zip(element_names, colors[:len(element_names)])}     # Формируем словарь данных для каждого элемента
    plot_combined_graph(ax, times, y_dict, 'Изменение количества атомов всех элементов')                                            # Строим объединенный график для всех элементов


# Подмодуль 5.2: Подготовка фигуры для отображения графиков

colors = ['blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'red', 'yellow', 'black', 'violet']  # Цвета для графиков
fig, ax = plt.subplots()  # Создаем фигуру и ось для построения графиков

def create_plot_functions(times, current_amounts, element_names, colors):
    """
    Создает список функций для отображения графиков.
    Параметры:
    times (list): Список значений времени.
    current_amounts (dict): Словарь с количеством атомов для каждого элемента.
    element_names (list): Список названий элементов.
    colors (list): Список цветов для графиков элементов.
    Возвращает:
    list: Список функций для отображения графиков.
    """
    plot_functions = []  # Создаем пустой список для хранения функций
    
    for element, color in zip(element_names, colors[:len(element_names)]):      # Создаем функцию для каждого элемента, добавляя её в список функций
        def single_element_plot(ax=ax, times=times, current_amounts=current_amounts, element=element, color=color):
            create_single_element_plot(ax, times, current_amounts, element, color)
        plot_functions.append(single_element_plot)                              # Добавляем функцию отображения одного элемента в список
    
    def combined_plot(ax=ax, times=times, current_amounts=current_amounts, element_names=element_names, colors=colors): # Создаем функцию для объединенного графика всех элементов
        create_combined_plot(ax, times, current_amounts, colors, element_names)
    plot_functions.append(combined_plot)                                        # Добавляем функцию объединенного графика в список
    return plot_functions                                                       # Возвращаем список функций

plot_functions = create_plot_functions(times, current_amounts, element_names, colors)   # Получаем список функций для отображения графиков

def on_click(event):
    """
    Обрабатывает двойной щелчок мыши для переключения графиков.
    Параметры:
    event (matplotlib.backend_bases.Event): Событие щелчка мыши.
    """
    global current_index
    if event.dblclick:                                                  # Проверяем, что был двойной щелчок
        current_index = (current_index + 1) % len(plot_functions)       # Переключаемся на следующий график
        plot_functions[current_index](ax)                               # Отображаем выбранный график

def on_key(event):
    """
    Обрабатывает нажатие пробела для закрытия графика.
    Параметры:
    event (matplotlib.backend_bases.Event): Событие нажатия клавиши.
    """
    if event.key == ' ':    # Проверяем, что нажата клавиша пробела
        plt.close()         # Закрываем график

fig.canvas.mpl_connect('button_press_event', on_click)  # Подключаем обработчик кликов мыши
fig.canvas.mpl_connect('key_press_event', on_key)  # Подключаем обработчик нажатий клавиш

current_index = 0                   # Начинаем с первого графика
plot_functions[current_index](ax)   # Отображаем первый график
plt.show()                          # Показываем график
