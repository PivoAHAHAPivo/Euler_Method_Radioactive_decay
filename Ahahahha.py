import numpy as np
import matplotlib.pyplot as plt

# Параметры системы
half_lives = [50, 0.00035, 0.0005, 40, np.inf]  # Периоды полураспада (лет)    разница между периодами распада должно быть не более 300000 раз
initial_nuclei = [1000000, 0, 0, 100000, 0]        # Начальное количество ядер
time_step = 0.001                          # Шаг времени (лет) для шага нужа разница в 3 раза для самого маленького периода полуаспада
total_time = 150                           # Общее время моделирования (лет)

# Константы распада
decay_constants = [np.log(2) / T if T != np.inf else 0 for T in half_lives]

# Время
time = np.arange(0, total_time, time_step)

# Инициализация массивов для хранения количества ядер
N = np.zeros((len(time), len(half_lives)))
N[0] = initial_nuclei

# Численное решение системы уравнений методом Эйлера
for t in range(1, len(time)):
    dN1 = -decay_constants[0] * N[t-1, 0]
    dN2 = decay_constants[0] * N[t-1, 0] - decay_constants[1] * N[t-1, 1]
    dN3 = decay_constants[1] * N[t-1, 1] - decay_constants[2] * N[t-1, 2]
    dN4 = decay_constants[2] * N[t-1, 2] - decay_constants[3] * N[t-1, 3]
    dN5 = decay_constants[3] * N[t-1, 3]
    
    N[t, 0] = N[t-1, 0] + dN1 * time_step
    N[t, 1] = N[t-1, 1] + dN2 * time_step
    N[t, 2] = N[t-1, 2] + dN3 * time_step
    N[t, 3] = N[t-1, 3] + dN4 * time_step
    N[t, 4] = N[t-1, 4] + dN5 * time_step

# Построение графиков
plt.figure(figsize=(10, 6))
for i in range(len(half_lives)):
    plt.plot(time, N[:, i], label=f'Элемент {i+1}')

plt.xlabel('Время (лет)')
plt.ylabel('Количество ядер')
plt.title('Радиоактивный распад в цепочке элементов с экстремально разными периодами полураспада')
plt.legend()
plt.grid(True)
plt.show()
