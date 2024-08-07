
    # Модуль 1
    # Установка нужных библиотек через терминал:

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
        # Подключение библиотек mplcursors
import mplcursors                               # Импортирует модуль mplcursors (Модуль предназначен для интерактивного курсора при рассмотрении графиков)s


    # Модуль 3: Ввод данных и их проверка
    # Подмодуль 3.1: Функции для проверки корректности вводимых данных
def input_elements(prompt):
    """
    Функция для получения списка элементов от пользователя через запятую.
    
    Параметры:
    prompt (str): Сообщение для запроса ввода.
    
    Возвращает:
    list: Список элементов, введенных пользователем.
    """
    while True:                                                             # Начинаем бесконечный цикл для постоянного запроса ввода до получения корректного значения
        try:                                                                # Начало блока try в котором будет попытка выполнения кода
            data = input(prompt).split(',')                                 # Получаем ввод от пользователя и разделяем строку по запятым
            if len(data) == 0:                                              # Проверка, что список не пустой
                raise ValueError("Список не может быть пустым.")            # Генерация исключения ValueError
            return data                                                     # Возвращаем список элементов
        except ValueError as e:                                             # Обрабатываем ошибку, если ввод некорректен начало блока except, перехватывает исключения 
                                                                            #   типа ValueError, которые были вызваны в блоке try. Переменная e содержит информацию об ошибке.
            print(f"Ошибка: {e}. Попробуйте снова.")                        # Выводим сообщение об ошибке

def input_positive_floats(prompt, count):
    """
    Функция для получения списка положительных чисел с плавающей точкой от пользователя.
    
    Параметры:
    prompt (str): Сообщение для запроса ввода.
    count (int): Ожидаемое количество значений.
    
    Возвращает:
    list: Список положительных чисел с плавающей точкой.
    """
    while True:                                                                         # Начинаем бесконечный цикл для постоянного запроса ввода до получения корректного значения
        try:                                                                            # Начало блока try в котором будет попытка выполнения кода
            data = list(map(float, input(prompt).split(',')))                           # Получаем ввод от пользователя, разделяем строку по запятым и конвертируем в float через
                                                                                        #   команду map и превращает результат в список через команду list и присваевает переменной data
            if len(data) != count:                                                      # Проверка, что количество введённых значений соответствует ожидаемому 
                raise ValueError(f"Должно быть введено {count} значений.")              # Генерация исключения ValueError для первого условия
            if any(x < 0 for x in data):                                                # Проверка, что все значения положительные
                raise ValueError("Все значения должны быть положительными числами.")    # Генерация исключения ValueError для второго условия
            return data                                                                 # Возвращаем список положительных чисел с плавающей точкой
        except ValueError as e:                                                         # Обрабатываем ошибку, если ввод некорректен
            print(f"Ошибка: {e}. Попробуйте снова.")                                    # Выводим сообщение об ошибке

def input_non_negative_integers(prompt, count):
    """
    Функция для получения списка неотрицательных целых чисел от пользователя.
    
    Параметры:
    prompt (str): Сообщение для запроса ввода.
    count (int): Ожидаемое количество значений.
    
    Возвращает:
    list: Список неотрицательных целых чисел.
    """
    while True:                                                                         # Начинаем бесконечный цикл для постоянного запроса ввода до получения корректного значения
        try:                                                                            # Начало блока try в котором будет попытка выполнения кода
            data = list(map(int, input(prompt).split(',')))                             # Получаем ввод от пользователя, разделяем строку по запятым и конвертируем в int
            if len(data) != count:                                                      # Проверка, что количество введённых значений соответствует ожидаемому
                raise ValueError(f"Должно быть введено {count} значений.")              # Генерация исключения ValueError для первого условия
            if any(x < 0 for x in data):                                                # Проверка, что все значения неотрицательные
                raise ValueError("Все значения должны быть неотрицательными целыми числами.")   # Генерация исключения ValueError для второго условия
            return data                                                                 # Возвращаем список неотрицательных целых чисел
        except ValueError as e:                                                         # Обрабатываем ошибку, если ввод некорректен
            print(f"Ошибка: {e}. Попробуйте снова.")                                    # Выводим сообщение об ошибке

def input_positive_float(prompt):
    """
    Функция для получения положительного числа с плавающей точкой от пользователя.
    
    Параметры:
    prompt (str): Сообщение для запроса ввода.
    
    Возвращает:
    float: Положительное число с плавающей точкой.
    """
    while True:                                                                     # Начинаем бесконечный цикл для постоянного запроса ввода до получения корректного значения
        try:                                                                        # Начало блока try в котором будет попытка выполнения кода
            data = float(input(prompt))                                             # Получаем ввод от пользователя и конвертируем в float
            if data <= 0:                                                           # Проверка, что значение положительное
                raise ValueError("Значение должно быть положительным числом.")      # Генерация исключения ValueError
            return data                                                             # Возвращаем положительное число с плавающей точкой
        except ValueError as e:                                                     # Обрабатываем ошибку, если ввод некорректен
            print(f"Ошибка: {e}. Попробуйте снова.")                                # Выводим сообщение об ошибке

def input_decay_types(prompt, count):
    """
    Функция для получения списка типов распада от пользователя.
    
    Параметры:
    prompt (str): Сообщение для запроса ввода.
    count (int): Ожидаемое количество значений.         
    
    Возвращает:
    list: Список типов распада ('alpha' или 'beta').
    """
    while True:                                                                     # Начинаем бесконечный цикл для постоянного запроса ввода до получения корректного значения
        try:                                                                        # Начало блока try в котором будет попытка выполнения кода
            data = input(prompt).split(',')                                         # Получаем ввод от пользователя и разделяем строку по запятым, создавая список значений
            if len(data) != count:                                                  # Проверка, что количество введенных значений соответствует ожидаемому
                raise ValueError(f"Должно быть введено {count} значений.")          # Генерация исключения ValueError для первого условия
            if any(x not in ['alpha', 'beta', 'none'] for x in data):                       # Проверка, что все значения являются 'alpha' или 'beta'
                raise ValueError("Все значения должны быть 'alpha' или 'beta'.")    # Генерация исключения ValueError для второго условия
            return data                                                             # Возвращаем список типов распада, если все проверки пройдены
        except ValueError as e:                                                     # Обрабатываем ошибку, если ввод некорректен
            print(f"Ошибка: {e}. Попробуйте снова.")                                # Выводим сообщение об ошибке

    # Подмодуль 3.2: Ввод данных пользователем
element_names = input_elements("Введите названия элементов (через запятую): ")                                              # Создание списка элементов
half_lives = input_positive_floats("Введите периоды полураспада (через запятую): ", len(element_names))                     # Создание списка периодов полураспада
initial_amounts = input_non_negative_integers("Введите начальные количества ядер (через запятую): ", len(element_names))    # Создание списка начального количества ядер
decay_types = input_decay_types("Введите типы распада для элементов (alpha или beta, через запятую): ", len(element_names)) # Создание списка типов распада
time_experiment = input_positive_float("Введите время эксперимента (в годах): ")                                            # Создание переменной времени эксперимента
time_step = input_positive_float("Введите шаг (в годах): ")                                                                 # Создание перменной шага для метода Эйлера


# Модуль 4: Введенние метода Эйлера для решения системы дифференциальных уравнений
# Подмодуль 4.1: Введение функций для рассчёта данных
def decay_constant(period):
    if period == 0:
        return float('inf')
    if period == float('inf'):
        return 0
    return np.log(2) / period

def initialize_values(N0_list, times):
    values = {name: np.zeros_like(times, dtype=float) for name in N0_list.keys()}
    for name in N0_list.keys():
        values[name][0] = N0_list[name]
    return values

def euler_step(N_list, decay_consts, decay_types, step, values, i, alpha_counts, beta_counts):
    for name in N_list.keys():
        if decay_consts[name] == float('inf'):
            decay_amount = values[name][i - 1]
            N_list[name] = 0
        else:
            decay_amount = decay_consts[name] * values[name][i - 1] * step
            N_list[name] -= decay_amount

        next_name = None
        if name != list(N_list.keys())[-1]:
            next_name = list(N_list.keys())[list(N_list.keys()).index(name) + 1]
        
        if next_name and decay_consts[name] != float('inf'):
            if decay_consts[next_name] != float('inf'):
                N_list[next_name] += decay_amount
            else:
                if decay_types[next_name] == 'alpha':
                    alpha_counts[i] += decay_amount
                elif decay_types[next_name] == 'beta':
                    beta_counts[i] += decay_amount
                N_list[next_name] += decay_amount

        if decay_types[name] == 'alpha':
            alpha_counts[i] += decay_amount
        elif decay_types[name] == 'beta':
            beta_counts[i] += decay_amount

        values[name][i] = N_list[name]

    return N_list

def euler_method_system(N0_list, decay_consts, decay_types, time, step):
    times = np.arange(0, time + step, step)
    values = initialize_values(N0_list, times)
    alpha_counts = np.zeros_like(times, dtype=float)
    beta_counts = np.zeros_like(times, dtype=float)
    
    N_list = {name: N0 for name, N0 in N0_list.items()}
    
    for i in range(1, len(times)):
        N_list = euler_step(N_list, decay_consts, decay_types, step, values, i, alpha_counts, beta_counts)

    return times, values, alpha_counts, beta_counts

# Создание словаря с элементами
decay_constants = {name: decay_constant(half_life) for name, half_life in zip(element_names, half_lives)}
initial_amounts_dict = {name: amount for name, amount in zip(element_names, initial_amounts)}
decay_types_dict = {name: decay_type for name, decay_type in zip(element_names, decay_types)}

# Расчет и заполнение данных
times, current_amounts, alpha_counts, beta_counts = euler_method_system(initial_amounts_dict, decay_constants, decay_types_dict, time_experiment, time_step)

# Функция для нахождения максимумов на графике
def find_maxima(y, t):
    maxima = []
    for i in range(1, len(y) - 1):
        if y[i - 1] < y[i] > y[i + 1]:
            maxima.append((t[i], y[i]))
    return maxima

# Функция для отображения графика
def plot_graph(ax, x, y, label, title, color='blue'):
    ax.clear()
    ax.plot(x, y, label=label, color=color)
    ax.set_xlabel('Время (годы)')
    ax.set_ylabel('Количество атомов')
    ax.set_title(title)
    ax.legend()
    ax.axhline(np.mean(y), color='r', linestyle='--', label='Среднее значение')
    ax.legend()
    cursor = mplcursors.cursor(ax, hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f'{label}\nВремя: {sel.target[0]:.2f} лет\nКол-во: {sel.target[1]:.2e}'))
    maxima = find_maxima(y, x)
    for t, value in maxima:
        ax.plot(t, value, 'ro')
    plt.draw()

# Функция для отображения объединенного графика
def plot_combined_graph(ax, x, y_dict, title):
    ax.clear()
    for label, (y, color) in y_dict.items():
        ax.plot(x, y, label=label, color=color)
    ax.set_xlabel('Время (годы)')
    ax.set_ylabel('Количество атомов')
    ax.set_title(title)
    ax.legend()
    plt.draw()

# Функция для переключения графиков
current_index = 0
def on_click(event):
    global current_index
    if event.dblclick:
        current_index = (current_index + 1) % len(figs)
        figs[current_index](ax)

# Функция для завершения показа графиков
def on_key(event):
    if event.key == ' ':
        plt.close()

# Присвоение цветов графикам
colors = ['blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'red', 'yellow', 'black', 'violet']

# Подготовка фигур
fig, ax = plt.subplots()

figs = [lambda ax=ax, times=times, current_amounts=current_amounts, element=element, color=color: plot_graph(ax, times, current_amounts[element], element, f'Изменение количества атомов {element}', color) for element, color in zip(element_names, colors[:len(element_names)])]

figs.append(lambda ax=ax, times=times, y_dict={element: (current_amounts[element], color) for element, color in zip(element_names, colors[:len(element_names)])}: plot_combined_graph(ax, times, y_dict, 'Изменение количества атомов всех элементов'))

figs.append(lambda ax=ax, times=times, alpha_counts=alpha_counts: plot_graph(ax, times, alpha_counts, 'alpha-распад', 'Количество alpha-частиц', 'red'))

figs.append(lambda ax=ax, times=times, beta_counts=beta_counts: plot_graph(ax, times, beta_counts, 'beta-распад', 'Количество beta-частиц', 'blue'))

# Обработчики событий
fig.canvas.mpl_connect('button_press_event', on_click)
fig.canvas.mpl_connect('key_press_event', on_key)

# Отображение первого графика
figs[current_index](ax)
plt.show()