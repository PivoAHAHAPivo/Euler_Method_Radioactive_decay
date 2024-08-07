import numpy as np

def input_elements(prompt):
    """Запрашивает у пользователя названия элементов, разделенные запятой."""
    while True:
        try:
            data = input(prompt).split(',')
            data = [el.strip() for el in data if el.strip()]
            if not data:
                raise ValueError("Список не может быть пустым.")
            return data
        except ValueError as e:
            print(f"Ошибка: {e}. Попробуйте снова.")

def input_positive_floats(prompt, count):
    """Запрашивает у пользователя положительные вещественные числа, разделенные запятой."""
    while True:
        try:
            data = list(map(float, input(prompt).split(',')))
            if len(data) != count:
                raise ValueError(f"Должно быть введено {count} значений.")
            if any(x < 0 and x != float('inf') for x in data):
                raise ValueError("Все значения должны быть положительными числами или бесконечными.")
            return data
        except ValueError as e:
            print(f"Ошибка: {e}. Попробуйте снова.")

def input_non_negative_integers(prompt, count):
    """Запрашивает у пользователя неотрицательные целые числа, разделенные запятой."""
    while True:
        try:
            data = list(map(int, input(prompt).split(',')))
            if len(data) != count:
                raise ValueError(f"Должно быть введено {count} значений.")
            if any(x < 0 for x in data):
                raise ValueError("Все значения должны быть неотрицательными целыми числами.")
            return data
        except ValueError as e:
            print(f"Ошибка: {e}. Попробуйте снова.")

def input_positive_float(prompt):
    """Запрашивает у пользователя положительное вещественное число."""
    while True:
        try:
            data = float(input(prompt))
            if data <= 0 and data != float('inf'):
                raise ValueError("Значение должно быть положительным числом или бесконечным.")
            return data
        except ValueError as e:
            print(f"Ошибка: {e}. Попробуйте снова.")

def create_element_dict(names, half_lives, initial_amounts):
    """Создает словарь из введенных данных."""
    element_dict = {}
    for i in range(len(names)):
        element_dict[names[i]] = {
            'half_life': half_lives[i],
            'initial_amount': initial_amounts[i],
        }
    return element_dict


def filter_elements(element_dict):
    """Фильтрует элементы и передает количество ядер от элементов с нулевым периодом полураспада к следующим элементам."""
    filtered_dict = {}
    last_amount = 0
    
    for el, params in element_dict.items():
        half_life = params['half_life']
        if half_life == 0:
            last_amount += params['initial_amount']
        else:
            if half_life != float('inf'):
                filtered_dict[el] = {
                    'half_life': half_life,
                    'initial_amount': last_amount + params['initial_amount'],
                }
                last_amount = 0
            else:
                filtered_dict[el] = {
                    'half_life': half_life,
                    'initial_amount': last_amount + params['initial_amount'],
                }
                last_amount = 0

    return filtered_dict


import numpy as np


def calculate_decay_constants(element_dict):
    """Вычисляет константы распада для элементов в словаре."""
    decay_constants = {}
    for element, params in element_dict.items():
        half_life = params['half_life']
        if half_life == float('inf'):
            decay_constants[element] = 0
        else:
            decay_constants[element] = np.log(2) / half_life
    return decay_constants

def euler_method_divided(element_dict, time_experiment, time_step):
    """Решает дифференциальные уравнения методом Эйлера, разделяя элементы на три группы."""
    decay_constants = calculate_decay_constants(element_dict)
    
    # Список элементов и их начальные значения
    elements = list(element_dict.keys())
    num_elements = len(elements)
    
    # Инициализация массивов для хранения значений
    num_steps = int(time_experiment / time_step) + 1
    element_arrays = {el: np.zeros(num_steps) for el in elements}
    
    # Установка начальных значений
    for el in elements:
        element_arrays[el][0] = element_dict[el]['initial_amount']
    
    for i in range(num_steps - 1):
        current_values = {el: element_arrays[el][i] for el in elements}
        
        # Первая группа: первый элемент
        first_element = elements[0]
        rates = {first_element: -decay_constants[first_element] * current_values[first_element]}
        
        # Вторая группа: элементы от второго до предпоследнего
        for j in range(1, num_elements - 1):
            el = elements[j]
            prev_element = elements[j - 1]
            next_element = elements[j + 1]
            
            rates[el] = decay_constants[prev_element] * current_values[prev_element] - decay_constants[el] * current_values[el]
        
        # Третья группа: последний элемент
        last_element = elements[-1]
        rates[last_element] = decay_constants[elements[-2]] * current_values[elements[-2]]
        
        # Обновление количества атомов для каждого элемента
        for el in elements:
            element_arrays[el][i + 1] = current_values[el] + time_step * rates.get(el, 0)
        

    return element_arrays

# Пример использования

# Получение данных от пользователя
element_names = input_elements("Введите названия элементов (через запятую): ")
half_lives = input_positive_floats("Введите периоды полураспада (через запятую): ", len(element_names))
initial_amounts = input_non_negative_integers("Введите начальные количества ядер (через запятую): ", len(element_names))
time_experiment = input_positive_float("Введите время эксперимента (в годах): ")
time_step = input_positive_float("Введите шаг (в годах): ")

# Создание словаря элементов
element_dict = create_element_dict(element_names, half_lives, initial_amounts)

# Фильтрация элементов
filtered_dict = filter_elements(element_dict)

# Решение методом Эйлера
element_arrays = euler_method_divided(filtered_dict, time_experiment, time_step)




import matplotlib.pyplot as plt

def plot_results(element_arrays, time_step):
    """Отображает графики результатов симуляции."""
    num_steps = int(time_experiment/time_step)
    time = np.arange(0, num_steps * time_step + time_step, time_step)

    # Построение графиков количества ядер для каждого элемента
    plt.figure(figsize=(14, 10))
    
    for el, values in element_arrays.items():
        plt.plot(time, values, label=f'{el}')
    
    plt.xlabel('Время (годы)')
    plt.ylabel('Количество ядер')
    plt.title('Изменение количества ядер элементов со временем')
    plt.legend()
    plt.grid(True)
    plt.show()


# Пример использования
plot_results(element_arrays, time_step)
