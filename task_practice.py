import math
import random
from random import randint
e,y,r=2.71,random.randint,random.randint
first=math.exp(y + r)
second=7.2*math.sin(r)
result=first + second
print("Жауабы:",result)


def medium_level():
    e,y,p=2.71,int(input()),int(input())
    cubing=3*y**2
    sqrt=math.sqrt(y + 1)

    log=math.log(p + y)
    exp=math.exp(p)

    first_calculation=(cubing + sqrt)

    second_calculation=(log + exp)

    result=first_calculation / second_calculation
    print(f"N =",result)

def high_level():
    import math
    import random
    # a)
    x = random.uniform(0.1, 1)
    if x <= 0:
        print("Қате: x логарифм үшін оң сан болуы керек.")
        return
    # b)
    sum_of = (3 + x) ** 6
    sqrt = math.sqrt(sum_of)
    lg = math.log(x)

    # c)
    minus = sqrt - lg
    exp = math.exp(0)
    square = 6 * x ** 2
    # d) Арксинус үшін мәннің [-1, 1] ауқымында екенін тексеру
    if -1 <= square <= 1:
        arc = math.asin(square)
    else:
        print("Қате: 6*x**2 нәтижесі arcsine функциясының ауқымынан тыс (-1, 1).")
        return
    plus = exp + arc
    # e)
    if plus == 0:
        print("Қате: Бөлгіш нөлге тең, нөлге бөлу мүмкін емес.")
        return
    # f)
    result_is = minus / plus
    print(f"K = {result_is}")



import math

# Определение функции k
import math

def k(e, arcsin6x2):
    # Lambda функциясының анықтамасы sqrt_expr
    sqrt_expr = lambda x: pow((3 + x) ** 6 - math.log(x), 0.5)

    # Орнату нүктесі мәндері x
    x_values = [0.5]

    # Әрбір x мәні үшін sqrt_expr мәнін есептеу
    sqrt_values = map(sqrt_expr, x_values)

    # Әрбір sqrt_expr мәні үшін K есептеңіз
    K_values = map(lambda sqrt_value: (sqrt_value + e) / (1 + arcsin6x2), sqrt_values)

    return list(K_values)

# # e және arcsin6x2 аргументтері берілген k функциясын шақыру
# e_value = 2
# arcsin6x2_value = 3
# result = k(e_value, arcsin6x2_value)
# print("k функциясын есептеу нәтижесі:", result)
import time, math

def calculate_k(e, arcsin6x2):
    # sqrt((3+x)^6-ln~x) мәндерін есептеу для x = 1
    x = 1
    sqrt_value = pow((3 + x) ** 6 - math.log(x), 0.5)

    # K мәнін есептеу
    K = (sqrt_value + e) / (1 + arcsin6x2)

    return K


def low_level():
    a=int(input()) ** 3
    b=int(input()) ** 3

    result= (a + b) / 2
    print("Без модуля",result)
    module=math.fabs(result)
    print("С модулем",module)



def second_part2_level_medium_task():
    t=3
    b=4.2
    x=int(input())
    a=int(input())

    log=math.log(math.fabs(x + a**2))

    calc=log ** 5

    ax=t**2*(math.sqrt(math.fabs(a + b)))
    bx=t + b**3
    print(f"First calculation: {calc}")
    print(f"Second calculation: {ax}")
    print(f"Thirty calculation: {bx}")


def second_part2_level_high_task():
    profit_last_month=10000
    cost_last_month=500


    cost_current_month=cost_last_month * 0.95

    # табыстылық
    profitability=(profit_last_month / cost_current_month) *100

    # Нәтиженің шығуы
    print(f"Кәсіпорынның ағымдағы айдағы табыстылығы: {profitability:.2f}%")


def thirt_part3_level_basic_task():
    import numpy as np

    # Функция для вычисления y = 1/x^2
    def function_value(x):
        if x == 0:
            return None  # Undefined
        return 1 / (x ** 2)

    # Логическая проверка области определения (D)
    def domain(x):
        return x != 0

    # Логическая проверка области изменения (R)
    def range_of_function(y):
        if y is None:
            return False
        return y > 0

    # Проверка и вывод результатов
    x_values = [-2, -1, 0, 1, 2]

    print("Область определения (D):")
    for x in x_values:
        print(f"x = {x}, x != 0: {domain(x)}")

    print("\nОбласть изменения (R):")
    for x in x_values:
        y = function_value(x)
        print(f"x = {x}, y = {y}, y > 0: {range_of_function(y)}")



def thirt_part3_level_medium_task():
    a,b,c,d=1,2,3,4


    div_to_5=(a % 5 == 0) or (b % 5 == 0) or (c % 5 == 0) or (d % 5 == 0)

    even_nums=(a % 2 == 0) or (b % 2 == 0) or (c % 2 == 0) or (d % 2 == 0)

    print(div_to_5,even_nums)

# a = 20
# b = 10
# c = 15
# d = 20
#
# result = thirt_part3_level_medium_task(a, b, c, d)
# print(result)

def math_fucntion():
    import matplotlib.pyplot as plt
    import numpy as np

    x = np.linspace(-10, 10, 400)
    y = x ** 2

    plt.plot(x, y, label='y = x^2')

    plt.axhline(y=0, color='b', linestyle='--', label='y = 50')
    plt.axvline(x=0,color='b')
    plt.axvline(x=2,color='b')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График функции y = x^2 ж\е y = 50')

    plt.grid(True)

    plt.legend()

    plt.show()


# Условные операторы

def low_level_operators():
    n = int(input())
    print("a) " + ("Yes" if n % 2 == 0 else "No"))
    print("b) " + ("Yes" if n % 10 == 7 else "No"))

def medium_level_operators():
    a,b,c=int(input()),int(input()),int(input())

    try:
        print("Введите три числа")
        print("Наибольшее из них",max(a,max(b,c)))
    except KeyboardInterrupt:
        print("что то не так")

def high_level_operators():
    # Ввод координат точки A (x1, y1)
    x1 = 5
    y1 = 6

    # Проверка условий
    if y1 <= 1 and y1 >= x1 and y1 >= -x1:
        print("Точка A ({}, {}) попадает в область.".format(x1, y1))
    else:
        print("не попадает в область.".format(x1, y1))



def choose_operators_basic_level():
    possible_resistances = [3, 12]  # Сопротивления, которые можно получить с двумя резисторами по 6 кОм

    # Первый набор сопротивлений
    R1, R2, R3 = 6, 10, 2
    print(f"Набор 1: R1={R1}, R2={R2}, R3={R3}")
    for R in [R1, R2, R3]:
        if R in possible_resistances:
            print(f"Сопротивление {R} кОм можно получить.")
        else:
            print(f"Сопротивление {R} кОм нельзя получить.")

    print()

    # Второй набор сопротивлений
    R1, R2, R3 = 3, 5, 7
    print(f"Набор 2: R1={R1}, R2={R2}, R3={R3}")
    for R in [R1, R2, R3]:
        if R in possible_resistances:
            print(f"Сопротивление {R} кОм можно получить.")
        else:
            print(f"Сопротивление {R} кОм нельзя получить.")

    print()

    # Третий набор сопротивлений
    R1, R2, R3 = 4, 12, 8
    print(f"Набор 3: R1={R1}, R2={R2}, R3={R3}")
    for R in [R1, R2, R3]:
        if R in possible_resistances:
            print(f"Сопротивление {R} кОм можно получить.")
        else:
            print(f"Сопротивление {R} кОм нельзя получить.")

def choose_operators_level_medium_level():
    import math

    def compute_y(a, b, z, x):
        if x <= a:
            return a ** 3 + math.atan(math.sin(b * x) ** 3) + math.cos(x ** 2) ** 2
        elif a < x < math.log(b):
            return math.sqrt(a + b * x) + 2 + math.sin(z * x)
        elif x >= math.log(b):
            return math.atan(a + b * x + z)

    # Параметры из задачи
    params = [
        (1.5, 5.7, math.tan(math.atan(5.7 * 1.5))),
        (3.7, 8.4, math.tan(math.atan(8.4 * 3.7))),
        (4.4, 5.6, math.tan(math.atan(5.6 * 4.4)))
    ]

    # Тестирование функции для различных значений x
    test_x = [0.5, 2, 5, 7, 10]

    for a, b, z in params:
        print(f"\nParameters: a={a}, b={b}, z={z}")
        for x in test_x:
            y = compute_y(a, b, z, x)
            print(f"f({x}) = {y}")


def operators_for_basic_level(N):
    min_digit = 9  # Изначально задаем максимальное возможное значение для цифры в десятичной системе

    for number in range(10, N + 1):
        # Преобразуем число в строку, чтобы пройтись по каждой его цифре
        for digit in str(number):
            # Преобразуем цифру обратно в число и сравниваем с текущей минимальной цифрой
            if int(digit) < min_digit:
                min_digit = int(digit)

    return min_digit


# Ввод значения N
# N = int(input("Введите значение N: "))
#
# # Поиск наименьшей цифры
# result = operators_for_basic_level(N)
#
# # Вывод результата
# print("Наименьшая цифра среди чисел от 10 до", N, ":", result)


import math


def operators_for_medium_level(k):
    A = 1  # Изначально произведение равно 1

    for j in range(1, k + 1):
        inner_sum = 0

        for i in range(j, k + 2):
            inner_sum += (math.pow(i + 5, 1 / 3)) / (i - 1)

        A *= ((j - 4) * j) / (j - 3) * inner_sum

    return A


# # Ввод значения k
# k = int(input("Введите значение k: "))
#
# # Вычисление A
# result = operators_for_medium_level(k)
#
# # Вывод результата
# print("Значение A:", result)

def operators_precondition_basic_level(m, n):
    total_sum = 0
    for number in range(m, n + 1):
        if number % 2 == 0:
            total_sum += number ** 2
    return total_sum


# # Ввод значений m и n
# m = int(input("Введите значение m: "))
# n = int(input("Введите значение n: "))
#
# # Вычисление суммы квадратов четных чисел
# result = operators_precondition_basic_level(m, n)
#
# # Вывод результата
# print("Сумма квадратов четных чисел в интервале от", m, "до", n, "равна", result)

def operators_precondition_medium_level():
    pass
