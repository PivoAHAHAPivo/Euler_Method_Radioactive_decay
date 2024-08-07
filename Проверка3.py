import numpy as np
import matplotlib.pyplot as plt
import mplcursors

# Универсальная функция для ввода данных
def input_data(prompt, dtype=float, condition=lambda x: x > 0):
    while True:
        try:
            data = list(map(dtype, input(prompt).split(',')))
            if not data:
                raise ValueError("Список не может быть пустым.")
            if not all(condition(x) or x == float('inf') for x in data):
                raise ValueError("Некоторые значения не соответствуют условию.")
            return data
        except ValueError as e:
            print(f"Ошибка: {e}. Попробуйте снова.")

# Ввод данных от пользователя
element_names = input_data("Введите названия элементов (через запятую): ", dtype=str, condition=lambda x: True)
half_lives = input_data(f"Введите периоды полураспада (через запятую для {len(element_names)} элементов): ", condition=lambda x: x >= 0)
initial_amounts = input_data(f"Введите начальные количества ядер (через запятую для {len(element_names)} элементов): ", dtype=int, condition=lambda x: x >= 0)
time_experiment = input_data("Введите время эксперимента (в годах): ", dtype=float, condition=lambda x: x > 0)[0]
time_step = input_data("Введите шаг (в годах): ", dtype=float, condition=lambda x: x > 0)[0]

# Создание словаря элементов
def create_element_dict(names, half_lives, initial_amounts):
    return {name: {'half_life': h, 'initial_amount': a} for name, h, a in zip(names, half_lives, initial_amounts)}

# Фильтрация элементов
def filter_elements(element_dict):
    filtered_dict = {}
    last_amount = 0
    for el, params in element_dict.items():
        half_life = params['half_life']
        if half_life == 0:
            last_amount += params['initial_amount']
        else:
            filtered_dict[el] = {'half_life': half_life, 'initial_amount': last_amount + params['initial_amount']}
            last_amount = 0
    return filtered_dict

# Вычисление констант распада
def calculate_decay_constants(element_dict):
    return {element: (np.log(2) / params['half_life'] if params['half_life'] != float('inf') else 0) for element, params in element_dict.items()}

# Метод Эйлера
def euler_method_divided(element_dict, time_experiment, time_step):
    decay_constants = calculate_decay_constants(element_dict)
    elements = list(element_dict.keys())
    num_steps = int(time_experiment / time_step) + 1
    element_arrays = {el: np.zeros(num_steps) for el in elements}
    for el in elements:
        element_arrays[el][0] = element_dict[el]['initial_amount']
    for i in range(num_steps - 1):
        current_values = {el: element_arrays[el][i] for el in elements}
        rates = {elements[0]: -decay_constants[elements[0]] * current_values[elements[0]]}
        for j in range(1, len(elements) - 1):
            el = elements[j]
            rates[el] = decay_constants[elements[j - 1]] * current_values[elements[j - 1]] - decay_constants[el] * current_values[el]
        rates[elements[-1]] = decay_constants[elements[-2]] * current_values[elements[-2]]
        for el in elements:
            element_arrays[el][i + 1] = current_values[el] + time_step * rates.get(el, 0)
    return element_arrays

# Подготовка данных для графиков
def find_maxima(y, t):
    return [(t[i], y[i]) for i in range(1, len(y) - 1) if y[i - 1] < y[i] > y[i + 1]]

def plot_graph(ax, x, y, label, title, color='blue'):
    ax.plot(x, y, label=label, color=color)
    ax.set_xlabel('Время (годы)')
    ax.set_ylabel('Количество атомов')
    ax.set_title(title)
    ax.axhline(np.mean(y), color='r', linestyle='--', label='Среднее значение')
    cursor = mplcursors.cursor(ax, hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f'{label}\nВремя: {sel.target[0]:.2f} лет\nКол-во: {sel.target[1]:.2e}'))
    maxima = find_maxima(y, x)
    for t, value in maxima:
        ax.plot(t, value, 'ro')
    ax.legend()

def plot_combined_graph(ax, x, y_dict):
    for label, (y, color) in y_dict.items():
        ax.plot(x, y, label=label, color=color)
    ax.set_xlabel('Время (годы)')
    ax.set_ylabel('Количество атомов')
    ax.set_title('Изменение количества атомов всех элементов')
    ax.legend()

def create_plot_functions(times, current_amounts, element_names, colors):
    plot_functions = [
        lambda ax, element=el, color=color: plot_graph(ax, times, current_amounts[element], element, f'Изменение количества атомов {element}', color)
        for el, color in zip(element_names, colors[:len(element_names)])
    ]
    plot_functions.append(lambda ax: plot_combined_graph(ax, times, {el: (current_amounts[el], color) for el, color in zip(element_names, colors[:len(element_names)])}) )
    return plot_functions

# Создание и отображение графиков
fig, ax = plt.subplots()
element_dict = create_element_dict(element_names, half_lives, initial_amounts)
filtered_dict = filter_elements(element_dict)
current_amounts = euler_method_divided(filtered_dict, time_experiment, time_step)

# Отладочная информация для проверки содержимого current_amounts
print("Current amounts:", current_amounts)
print("Filtered dict:", filtered_dict)

# Убедимся, что все элементы присутствуют в current_amounts
for element in element_names:
    if element not in current_amounts:
        print(f"Ошибка: элемент '{element}' отсутствует в current_amounts.")

times = np.arange(0, time_experiment + time_step, time_step)
colors = ['blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'red', 'yellow', 'black', 'violet']

plot_functions = create_plot_functions(times, current_amounts, element_names, colors)

def on_click(event):
    global current_index
    if event.dblclick:
        current_index = (current_index + 1) % len(plot_functions)
        ax.clear()  # Очистка предыдущего графика
        plot_functions[current_index](ax)
        plt.draw()

def on_key(event):
    if event.key == ' ':
        plt.close()

fig.canvas.mpl_connect('button_press_event', on_click)
fig.canvas.mpl_connect('key_press_event', on_key)

current_index = 0
plot_functions[current_index](ax)
plt.show()
