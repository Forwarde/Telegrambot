import random
def math_fucntion():
    import matplotlib.pyplot as plt
    import numpy as np

    x = np.linspace(-10, 10, 400)
    y = x ** 2

    plt.plot(x, y, label='y = x^2')

    plt.axhline(y=0, color='b', linestyle='--', label='y = 50')
    plt.axvline(x=0,color='b')


    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График функции y = x^2 ж\е y = 50')

    plt.grid(True)

    plt.legend()

    plt.show()
math_fucntion()