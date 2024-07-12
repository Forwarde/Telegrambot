# # Define the bubble_sort function
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
#
# # Example usage
# my_list = [64, 34, 25, 12, 22, 11, 90]
# sorted_list = bubble_sort(my_list)
# print("Sorted list:", sorted_list)

def sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j+1] = arr[j + 1],arr[j]

    return arr

my_list=[1,8,2,5,4,9,0]
sorted_list=sort(my_list)
# print(sorted_list)

def sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j + 1] = arr[j+1],arr[j]

    return arr

my_list=[1,6,4,2,9,0,7,6]
sorted_list=sort(my_list)


def binary_search(arr, target):

    """
#     low = 0
#     high = len(arr) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#
#     return -1
#
#
# # Пример использования
# my_list = [1, 3, 5, 7, 9]
# target = 5
# result = binary_search(my_list, target)
# if result != -1:
#     print("Элемент найден в позиции:", result)
# else:
#     print("Элемент не найден")

# Определим класс для пользователя

class User:
    def __init__(self, age, name, user_id):
        self.age = age
        self.user_id = user_id
        self.name = name

def create_users():
    users = [
        User(102, 'Nurim', 22),
        User(103, 'Gven', 22),
        User(104, 'Pitter', 18),
        User(105, 'Zoro', 20)
    ]
    return users

# def binary_search(users, target):
#     low = 0
#     high = len(users) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         if users[mid].user_id == target:
#             return users[mid]
#         elif users[mid].user_id < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return None
#
# users = create_users()
# users.sort(key=lambda x: x.user_id)

# target = 22  # Здесь укажем user_id, который мы ищем
#
# search = binary_search(users, target)
# if search:
#     print("Yes")
# else:
#     print("No")
import math
# e=2.18
# y=1
# r=1
# Бзаовый уровень
def first_level():
    e,y,r=2.71,int(input("первое значение:")),int(input("Второе значение:"))
    first=math.exp(y + r)
    second=7.2*math.sin(r)
    w=first + second
    print(w)



# def calculate_w(y, r):
#     # 1. Возведение в степень
#     exponentiation = math.exp(y + r)
#
#     # 2. Сложение
#     summation = y + r
#
#     # 3. Синус
#     sine = math.sin(r)
#
#     # 4. Умножение
#     multiplication = 7.2 * sine
#
#     # 5. Сложение
#     w = exponentiation + multiplication
#
#     return w
#
# y = 1.0  # Пример значения y
# r = 2.0  # Пример значения r
#
# w = calculate_w(y, r)
# print(f"W = {w}")

# Средний уровень
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
    x=int(input())

    sum_of=(3 + x)**6

    sqrt=math.sqrt(sum_of)
    lg=math.log(x)

    minus=(sqrt - lg)

    exp=math.exp(0)
    square=6*x**2

    arc=math.asin(square)

    plus=exp + arc

    result_is=minus / plus

    print(f"K = {result_is}")


import math

def high_level():
    x = float(input("Введите значение x: "))

    if x <= 0:
        print("Ошибка: x должно быть положительным числом для логарифма.")
        return

    sum_of = (3 + x) ** 6
    sqrt = math.sqrt(sum_of)
    lg = math.log(x)

    minus = sqrt - lg
    exp = math.exp(0)
    square = 6 * x ** 2

    # Проверка, чтобы значение было в диапазоне [-1, 1] для арксинуса
    if -1 <= square <= 1:
        arc = math.asin(square)
    else:
        print("Ошибка: Результат 6*x**2 выходит за пределы допустимого диапазона для функции арксинуса (-1, 1).")
        return

    plus = exp + arc

    if plus == 0:
        print("Ошибка: Знаменатель равен нулю, деление на ноль невозможно.")
        return

    result_is = minus / plus
    print(f"K = {result_is}")

def low_level():
    a=int(input()) ** 3
    b=int(input()) ** 3

    result= (a + b) / 2
    print("Без модуля",result)
    module=math.fabs(result)
    print("С модулем",module)

low_level()











