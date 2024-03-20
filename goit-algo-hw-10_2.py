import numpy as np
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

# Визначення меж інтегрування
a = 0  # Нижня межа
b = 2  # Верхня межа

# Обчислення площі прямокутника
rectangle_area = (b - a) * max(f(np.linspace(a, b, 1000)))

# Кількість випробувань
num_samples = 10000

# Генерування випадкових точок
x_samples = np.random.uniform(a, b, num_samples)
y_samples = np.random.uniform(0, max(f(np.linspace(a, b, 1000))), num_samples)

# Підрахунок кількості точок, що потрапили під криву
points_under_curve = sum(f(x_samples) > y_samples)

# Обчислення відношення кількості точок під кривою до загальної кількості точок
ratio = points_under_curve / num_samples

# Обчислення значення інтеграла
integral_value = rectangle_area * ratio

print("Значення інтеграла методом Монте-Карло:", integral_value)

# Обчислення інтеграла
result, error = spi.quad(f, a, b)

print("Значення інтеграла, отримане за допомогою quad:", result)
