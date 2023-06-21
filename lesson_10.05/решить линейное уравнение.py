# Задание:
# решить линейное уравнение с помощью матрицы
# x + y + z = 62
# x + 5y - z = -4
# 2x - y + 3z = 27
# 1 1 1 6
# 2 5 -1 -4
# 2 -1 3 27
# AX = b
# inv(A)AX = inv(A)b
# EX = inv(A)b
# X = inv(A)b
import numpy as np


A = np.array([[1, 1, 1],
              [1, 5, -1],
              [2, -1, 3]])


b = np.array([62, -4, 27])


X = np.linalg.inv(A).dot(b)

print(X)

# Вывод
# [-361.  130.  293.]
