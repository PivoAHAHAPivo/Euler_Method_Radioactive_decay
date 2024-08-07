
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


    
    # Модуль 3: Ввод количества ядер радиоактивных веществ

    # Подмодуль 3.1: Функция для обработки вводимых данных
def get_valid_input(prompt):
    """
    Функция для получения валидного целого положительного числа от пользователя.
        Параметры:
    prompt (str): Сообщение для запроса ввода.
        Возвращает:
    int: Валидное целое положительное число.
    """
    while True:                                                     # Бесконечный цикл не закончится, пока не будет достигнуто правильное условие
        value = input(prompt)                                       # Создаёт переменную value, которая равна введённой переменной prompt
        if value.isdigit():                                         # Проверка, что ввод состоит только из цифр
            value = int(value)                                      # Даёт переменной value тип integer, если условие value.isdigit() True
            if value > 0:                                           # Проверка, что ведённое чило больше нуля
                return value                                        # Возвращаем значение, если условие value > 0 True
            elif value == 0:                                        # Проверка, что введённое число равно нулю
                return 0                                            # Возвращаем 0, если условие value > 0 False, а условие value == 0 True
        print("Введите целое положительное число.")                 # Сообщение об ошибке ввода, если условие value.isdigit() False

    # Подмодуль 3.2: Ввод значений для каждого элемента
elements = ["N_U_238", "N_Th_234", "N_Pa_234", "N_U_234", "N_Th_230",       # Определяет список в котором в каждой ячейке находится название переменных для введенных данных
            "N_Ra_226", "N_Rn_222", "N_Po_218", "N_Pb_214", "N_Bi_214", 
            "N_Po_214", "N_Pb_210", "N_Bi_210", "N_Po_210", "N_Pb_206"]

nuclei_counts = {}                          # Создаёт словарь с названием nuclei_count
for element in elements:                                                                    # Уловие цикла, для каждого элемента из списка elements
    nuclei_counts[element] = get_valid_input(f"Введите количество ядер для {element}: ")    # Через функцию get_valid_input добавляет введённое значение под ключом, 
                                                                                            #   соответствующим названию элемента
    


    # Модуль 4: Периоды полураспада и расчёт констант распада радиоактивных элементов

    # Список элементов с их периодами полураспада в годах и типами распада
elements = [                                    # Создаёт новый список elements, где каждая ячейка это каскад данных
    ("U_238", 10000, "Альфа распад"),
    ("Th_234", 1500, "Бета-минус распад"),
    ("Pa_234", 3000, "Бета-минус распад"),
    ("U_234", 1200, "Альфа распад"),
    ("Th_230", 2200, "Альфа распад"),
    ("Ra_226", 4500, "Альфа распад"),
    ("Rn_222", 1600, "Альфа распад"),
    ("Po_218", 2700, "Альфа распад"),
    ("Pb_214", 5500, "Бета-минус распад"),
    ("Bi_214", 3400, "Бета-минус распад"),
    ("Po_214", 1200, "Альфа распад"),
    ("Pb_210", 3300, "Бета-минус распад"),
    ("Bi_210", 2400, "Бета-минус распад"),
    ("Po_210", 1100, "Альфа распад"),
    ("Pb_206", float('inf'), "Стабильный элемент")  # Свинец-206 стабильный элемент
]
decay_constants = {}        # Словарь для хранения периодов полураспада и констант распада                                

    # Подмодуль 4.1: Расчёт констант распада
for element, hl, decay_type in elements:            # Условие цикла, для каждого element, hl, decay_type для каждого каскада в списке elements
    if hl > 0:                                      # Условие if при котороом проверяется если hl > 0
        decay_constants[element] = np.log(2) / hl   # Расчёт константы распада под ключом, есди условие выше True
    else:
        decay_constants[element] = 0

    # Подмодуль 4.2: Вывод рассчитанных значений
for element, hl, decay_type in elements:
    dc = decay_constants[element]                   # Присвивает переменной dc значение в словаре через ключ названия элемента
    print(f"{element}: период полураспада = {hl} лет, константа распада = {dc:.5e} 1/год ({decay_type})")       # Вывод в терминал данных



    # Модуль 5: Решение системы дифференциальных уравнений первого порядка методом Эйлера и расчет количества альфа и бета частиц

    # Определение переменных констант распада для использования в модуле 5
decay_constants = {el: dc for el, dc in decay_constants.items()}        # Создаёт копию словаря и возвращает пары (ключ, значение) с использованием словарных выражений 
                                                                        #   (dict comprehension). Словарь имеет те же ключи и значения просто доступные для рассчётов в дальнейшем.

    # Подмодуль 5.1: Введение начальных условий
alpha_particles = 0  # Начальное количество альфа-частиц
beta_particles = 0   # Начальное количество бета-частиц

    # Подмодуль 5.2: Функция для получения валидного целого положительного числа от пользователя
def get_valid_input_2(prompt_2):
    """
    Функция для получения валидного целого положительного числа от пользователя.
    Параметры:
    prompt_2 (str): Сообщение для запроса ввода.
    Возвращает:
    int: Валидное целое положительное число.
    """
    while True:                                             # Бесконечный цикл не закончится, пока не будет достигнуто правильное условие 
        value_2 = input(prompt_2)                           # Создаёт переменную value_2, которая равна введённой переменной prompt_2
        if value_2.isdigit() and int(value_2) > 0:          # Смешанное условие проверяющее если введённое значение состоит из цифр и больше ли оно нуля
            return int(value_2)                             # Возвращает значение типа integer, если условие value_2.isdigit() and int(value_2) > 0 True
        else:
            print("Введите целое положительное число.")     # Сообщение об ошибке ввода, если условие value_2.isdigit() and int(value_2) > 0 False

    # Подмодуль 5.3: Задание значения времени симуляции и шага для метода Эйлера
while True:                                                                     # Бесконечный цикл не закончится, пока не будет достигнуто правильное условие
    T = get_valid_input_2("Время симуляции T в годах: ")                        # Ввод времени симуляции
    h = get_valid_input_2("Длина шага h в годах для метода Эйлера: ")           # Ввод длины шага
    if T / h >= 10:                                                             # Проверка, чтобы количество шагов было достаточно большим
        print(f"T: {T}, h: {h}")                                                # Вывод введённых значений, если условие T / h >= 10 True
        break                                                                   # Заканчивает цикл 
    else:
        print("Введите значения, отношение которых будет больше 100.")          # Сообщение об ошибке ввода, если условие T / h >= 10 False

N = T / h                                                   # Расчёт количества шагов для метода Эйлера
steps = int(round(N))                                       # Округление количества шагов до целого числа
print(f"Количество шагов для метода Эйлера N = {N}")        # Вывод количества шагов

    # Подмодуль 5.4: Создание массивов для хранения данных
time = np.zeros(steps + 1)                                          # Массив для хранения времени
elements = ['U_238', 'Th_234', 'Pa_234', 'U_234', 'Th_230', 'Ra_226', 'Rn_222', 'Po_218', 'Pb_214', 'Bi_214', 'Po_214', 'Pb_210', 'Bi_210', 'Po_210', 'Pb_206']
                                                                    # Новый список elements
element_arrays = {el: np.zeros(steps + 1) for el in elements}       # Массивы для каждого элемента задаётся значением в новый словарь element_arrays через ключ
alpha_arr = np.zeros(steps + 1)                                     # Массив для альфа-частиц
beta_arr = np.zeros(steps + 1)                                      # Массив для бета-частиц

    # Подмодуль 5.5: Инициализация массивов начальными условиями
    # Инициализация массивов начальными условиями
time[0] = 0                             # Начальное условие 0. Цикл для каждой ячейки массива при котором следующая ячейка имеет значение предыдущей плюс шаг h.
for i in range(steps):
    time[i + 1] = time[i] + h

for el in elements:                                         # Цикл для каждого елемента в списке elements. При котором через ключ проверяется наличие этого элемента и 
    key = f"N_{el}"                                         #   создаётся массив где на первую ячейку устанавливается наше введенное значение.
    if key in nuclei_counts:
        element_arrays[el][0] = nuclei_counts[key]

alpha_arr[0] = alpha_particles                              # Создает массив для альфа частиц и присваевает начальное значение в первую ячейку
beta_arr[0] = beta_particles

    # Подмодуль 5.6: Метод Эйлера для расчета данных и обновления значений
for i in range(steps):                                                          # Цикл для каждого i в диапазоне steps, так как первая ячейка занята начальным значением
    current_values = {el: element_arrays[el][i] for el in elements}             # Через словарь где значение это массивы данных. Текущие значения для каждого элемента (ключа).

    rates = {       # Расчёт скоростей распада для каждого элемента, при помощи списка rates
        'U_238': -decay_constants["U_238"] * current_values['U_238'],
        'Th_234': decay_constants["U_238"] * current_values['U_238'] - decay_constants["Th_234"] * current_values['Th_234'],
        'Pa_234': decay_constants["Th_234"] * current_values['Th_234'] - decay_constants["Pa_234"] * current_values['Pa_234'],
        'U_234': decay_constants["Pa_234"] * current_values['Pa_234'] - decay_constants["U_234"] * current_values['U_234'],
        'Th_230': decay_constants["U_234"] * current_values['U_234'] - decay_constants["Th_230"] * current_values['Th_230'],
        'Ra_226': decay_constants["Th_230"] * current_values['Th_230'] - decay_constants["Ra_226"] * current_values['Ra_226'],
        'Rn_222': decay_constants["Ra_226"] * current_values['Ra_226'] - decay_constants["Rn_222"] * current_values['Rn_222'],
        'Po_218': decay_constants["Rn_222"] * current_values['Rn_222'] - decay_constants["Po_218"] * current_values['Po_218'],
        'Pb_214': decay_constants["Po_218"] * current_values['Po_218'] - decay_constants["Pb_214"] * current_values['Pb_214'],
        'Bi_214': decay_constants["Pb_214"] * current_values['Pb_214'] - decay_constants["Bi_214"] * current_values['Bi_214'],
        'Po_214': decay_constants["Bi_214"] * current_values['Bi_214'] - decay_constants["Po_214"] * current_values['Po_214'],
        'Pb_210': decay_constants["Po_214"] * current_values['Po_214'] - decay_constants["Pb_210"] * current_values['Pb_210'],
        'Bi_210': decay_constants["Pb_210"] * current_values['Pb_210'] - decay_constants["Bi_210"] * current_values['Bi_210'],
        'Po_210': decay_constants["Bi_210"] * current_values['Bi_210'] - decay_constants["Po_210"] * current_values['Po_210'],
        'Pb_206': decay_constants["Po_210"] * current_values['Po_210']
    }

    # Обновление количества атомов для каждого элемента
    for el in elements:
        element_arrays[el][i + 1] = current_values[el] + h * rates[el]      # Рассчёт через метод Эйлера с испоьзованием словарей.

    # Обновление количества альфа- и бета-частиц
    alpha_arr[i + 1] = alpha_arr[i] + h * (
        decay_constants["U_238"] * current_values['U_238'] + 
        decay_constants["U_234"] * current_values['U_234'] +
        decay_constants["Th_230"] * current_values['Th_230'] +
        decay_constants["Ra_226"] * current_values['Ra_226'] +
        decay_constants["Rn_222"] * current_values['Rn_222'] +
        decay_constants["Po_218"] * current_values['Po_218'] +
        decay_constants["Po_214"] * current_values['Po_214'] +
        decay_constants["Po_210"] * current_values['Po_210']
    )
    beta_arr[i + 1] = beta_arr[i] + h * (
        decay_constants["Th_234"] * current_values['Th_234'] +
        decay_constants["Pa_234"] * current_values['Pa_234'] +
        decay_constants["Pb_214"] * current_values['Pb_214'] +
        decay_constants["Bi_214"] * current_values['Bi_214'] +
        decay_constants["Pb_210"] * current_values['Pb_210'] +
        decay_constants["Bi_210"] * current_values['Bi_210']
    )
    # Подмодуль 5.7: Вывод итоговых данных
print("Итоговые количества ядер элементов после времени T:")
for el in elements:
    print(f"{el}: {element_arrays[el][-1]:}")                       # Вывод последнего в списке каждого элемента значения.

print(f"Итоговое количество альфа частиц: {alpha_arr[-1]:.2f}")     # Вывод итогового количества альфа и бета частиц из списка
print(f"Итоговое количество бета частиц: {beta_arr[-1]:.2f}")



    # Модуль 6: Введение отображения графиков

        # Подмолдуль 6.1: Введение функции нахождения максимума графика
def find_maxima(y, t):                              # Определяет функцию find_maxima с аргументами y, t
    """
    Функция нахождения локального максимума графика функции
    Параметры:
    y[i](float): значение в ячейке массива текущих значений количества ядер каждого вещества
    t[i](float): значеие в ячейке массива текущего значения времени
    Возвращает: 
    maxima[(t[i], y[i])](list): список с картежем из двух значений
    """ 
    maxima = []                                     # Создаёт массив под названием maxima
    for i in range(1, len(y) - 1):                  # Функция for для каждого i в диапазоне от 1 до предпоследнего, чтобы не вылезти за границы массива
        if y[i - 1] < y[i] > y[i + 1]:              # Функция if, которая определяет локальный максимум на графике
            maxima.append((t[i], y[i]))             # Добавляет в список maxima кортеж (t[i], y[i]), где t[i] это время, а y[i] это количество ядер, если условие
                                                    #   if y[i - 1] < y[i] > y[i + 1]: True 
    return maxima                                   # Возвращает переменную со значением maxima и заканчивает цикл

        # Введение функций для отображения графика  
def plot_graph(ax, x, y, label, title, color = 'blue'):
    """
    Функция черчения графика на одном полотне
    Параматры:
    ax: представляет область где будет строится график. объект осей на котором будет строится график из библиотеки Matplotlib.
    x: массив значений по оси х представляющий время
    y: массив значений по оси у представляющий количество атомов
    label: метка для графика используемая в легенде
    titile: заголовок графика
    color: цвет линии графика по умолчанию синий
    Возвращает:
    plt.draw(): обновляет и отображает график
    """
    ax.clear()                                                  # Очистка осей перед построением нового графика
    ax.plot(x, y, label = label, color = color)                 # Строит график по данным из массивов x и y с меткой label
    ax.set_xlabel('Время (годы)')                               # Устанавливает надпись на осе x с названием Время (годы)
    ax.set_ylabel('Количество атомов')                          # Устанавливает надпись на осе y с названием Количество атомов
    ax.set_title(title)                                         # Устанавливает заголовок для каждого графика
    ax.legend()                                                 # Отображает легенду на графике
    ax.axhline(np.mean(y), color='r', linestyle='--', label='Среднее значение')
                                                                # Устанавливает среднюю линию. Добавляется горизонтальная линия на уровне среднего значения y, красного цвета с 
                                                                #   пунктирной линией и меткой Среднее значение.
    ax.legend()                                                 # Обновляет легенду и добавляет метку средней линии
    maxima = find_maxima(y, x)                                  # Вводит переменную maxima и присваевает ей значение функции find_maxima(y, x)
    for t, value in maxima:                                     # Условие for для значений t, value в переменной maxima (грубо говоря сравнивает значения)
        ax.plot(t, value, 'ro')                                 # Отображает на графике в виде красной точки все локальные максимумы
    plt.draw()                                                  # Отображает график на экране
                    # Пременная  ax нужна для связи всех функций чтобы переключение графиков работало корректно и было связвнно с осями графика. Одно полотно другие оси.

        # Введение функции для отображения нескольких графиков
def plot_combined_graph(ax, x, y_dict, title):
    """
    Функция черчения графиков на одном полотне
    Параматры:
    ax: представляет область где будет строится график. объект осей на котором будет строится график из библиотеки Matplotlib.
    x: массив значений по оси х представляющий время
    y_dict: словарь с ключами и значениями для обработки
    titile: заголовок графика
    Возвращает:
    plt.draw(): обновляет и отображает графики
    """
    ax.clear()                                          # Очистка осей перед построением нового графика
    for label, (y, color) in y_dict.items():            # Условие for для каждого label, (y, color) из словаря y_dict. y_dict.items() возвращает пары (ключ, значение) из y_dict.
                                                        #   Где label это ключ, а (y, color) это значение.
        ax.plot(x, y, label=label, color=color)         # Строит графики по данным из массивов x и y с метками label и цветами color
    ax.set_xlabel('Время (годы)')                       # Устанавливает надпись на оси x с названием Время (годы)
    ax.set_ylabel('Количество атомов')                  # Устанавливает надпись на оси y с названием Количество атомов
    ax.set_title(title)                                 # Устанавливает заголовок для графика
    ax.legend()                                         # Отображает легенду на графике
    plt.draw()                                          # Обновляет фигуру

figs = [                                                                                                        # Введение списка графиков        
    lambda ax: plot_graph(ax, time, element_arrays['U_238'], 'U-238', 'Распад U-238', color='blue'),
    lambda ax: plot_graph(ax, time, element_arrays['Th_234'], 'Th-234', 'Распад Th-234', color='green'),
    lambda ax: plot_graph(ax, time, element_arrays['Pa_234'], 'Pa-234', 'Распад Pa-234', color='orange'),
    lambda ax: plot_graph(ax, time, element_arrays['U_234'], 'U-234', 'Распад U-234', color='purple'),
    lambda ax: plot_graph(ax, time, element_arrays['Th_230'], 'Th-230', 'Распад Th-230', color='cyan'),
    lambda ax: plot_graph(ax, time, element_arrays['Ra_226'], 'Ra-226', 'Распад Ra-226', color='magenta'),
    lambda ax: plot_graph(ax, time, element_arrays['Rn_222'], 'Rn-222', 'Распад Rn-222', color='yellow'),
    lambda ax: plot_graph(ax, time, element_arrays['Po_218'], 'Po-218', 'Распад Po-218', color='brown'),
    lambda ax: plot_graph(ax, time, element_arrays['Pb_214'], 'Pb-214', 'Распад Pb-214', color='pink'),
    lambda ax: plot_graph(ax, time, element_arrays['Bi_214'], 'Bi-214', 'Распад Bi-214', color='gray'),
    lambda ax: plot_graph(ax, time, element_arrays['Po_214'], 'Po-214', 'Распад Po-214', color='black'),
    lambda ax: plot_graph(ax, time, element_arrays['Pb_210'], 'Pb-210', 'Распад Pb-210', color='red'),
    lambda ax: plot_graph(ax, time, element_arrays['Bi_210'], 'Bi-210', 'Распад Bi-210', color='darkblue'),
    lambda ax: plot_graph(ax, time, element_arrays['Po_210'], 'Po-210', 'Распад Po-210', color='darkgreen'),
    lambda ax: plot_graph(ax, time, element_arrays['Pb_206'], 'Pb-206', 'Распад Pb-206', color='darkorange'),
    lambda ax: plot_graph(ax, time, alpha_arr, 'Альфа частицы', 'Количество альфа частиц', color='purple'),
    lambda ax: plot_graph(ax, time, beta_arr, 'Бета частицы', 'Количество бета частиц', color='cyan'),
    lambda ax: plot_combined_graph(ax, time, {
        'U-238': (element_arrays['U_238'], 'blue'),
        'Th-234': (element_arrays['Th_234'], 'green'),
        'Pa-234': (element_arrays['Pa_234'], 'orange'),
        'U-234': (element_arrays['U_234'], 'purple'),
        'Th-230': (element_arrays['Th_230'], 'cyan'),
        'Ra-226': (element_arrays['Ra_226'], 'magenta'),
        'Rn-222': (element_arrays['Rn_222'], 'yellow'),
        'Po-218': (element_arrays['Po_218'], 'brown'),
        'Pb-214': (element_arrays['Pb_214'], 'pink'),
        'Bi-214': (element_arrays['Bi_214'], 'gray'),
        'Po-214': (element_arrays['Po_214'], 'black'),
        'Pb-210': (element_arrays['Pb_210'], 'red'),
        'Bi-210': (element_arrays['Bi_210'], 'darkblue'),
        'Po-210': (element_arrays['Po_210'], 'darkgreen'),
        'Pb-206': (element_arrays['Pb_206'], 'darkorange')
    }, 'Совокупность всех элементов')
]

        # Подмодуль 6.2: Введение возможности пропуска графиков
        # Определение начальных условий
current_index = 0                                               # Устанавливает начальное значение индекса в списке как 0
        # Введение функции переключения графиков
def on_click(event):                                            # Определяет функцию on_click с аргументом event (событие)
    global current_index                                        # Пременная current_index является глобальной для этой функции
    if event.dblclick:                                          # Условие if event.dblclick: при котором проверяется если было событие event. двойного нажания мыши dblclick
        current_index = (current_index + 1) % len(figs)         # Приравнивает переменную current_index к значению (current_index + 1) % len(figs). (current_index + 1) % len(figs)
                                                                #   является специальной для зацикливания графика. Делит current_index + 1 на длину списка (len(figs)) и берёт
                                                                #   её остаток. Так как длина списка на один больше чем последний индекс списка то цикл всегда имеет значения от 0 
                                                                #   до len(figs) - 1.
        figs[current_index](ax)                                 # Вызывает функцию из списка figs[] на позиции current_index с аргументом ax
        # Введение функции прекращения показа графиков
def on_key(event):                                              # Определяет функцию on_key с аргументом event (событие)
    if event.key == ' ':                                        # Условие if event,key == ' ': при котором проверяетсяесли было событие event. нажатия клавиши пробел key == ' '
        plt.close()                                             # Команда закрытия шаблона с графиками
        
        # Введение событий
fig, ax = plt.subplots(1, 1, figsize=(16, 9))                   # Создает фигуру и оси для построения графика через команду plt.subplots(1, 1, figsize=(16, 9))
fig.canvas.mpl_connect('key_press_event', on_key)               # fig.canvas: Объект холста (canvas) фигуры, на котором отрисовываются графики.
                                                                #   mpl_connect: Метод, который позволяет подключить обработчики событий к холсту.
                                                                #   'key_press_event': Событие, которое происходит при нажатии клавиши на клавиатуре.
                                                                #   on_key: Функция, которая будет вызвана при наступлении события 'key_press_event'. 
                                                                #   Эта функция должна быть определена заранее и принимать один аргумент — объект события.
fig.canvas.mpl_connect('button_press_event', on_click)          # 'button_press_event': Событие, которое происходит при нажатии кнопки мыши на холсте.
                                                                #   on_click: Функция, которая будет вызвана при наступлении события 'button_press_event'. 
                                                                #   Эта функция также должна быть определена заранее и принимать один аргумент — объект события.
        # Запуск первого графика
figs[current_index](ax)                                         # Вызывает функцию из списка figs[] на позиции current_index с аргументом ax
plt.show()                                                      # Вызывает отоброжение графиков построенных до этого

