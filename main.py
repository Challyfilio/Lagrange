import numpy as np
import matplotlib.pyplot as plt

# 拉格朗日插值计算
def Lagrange(data_x, data_y, dot_n, new_x):  # 输入插值点(x,y)坐标；dot_n:点个数；new_x:描点用
    parameters = []
    i = 0
    while i < dot_n:
        j = 0  # 控制做累乘
        temp = 1  # 分母乘积
        while j < dot_n:
            if (i != j):
                temp *= data_x[i] - data_x[j]
            j += 1
        parameters.append(data_y[i] / temp)  # 系数列表，y/分母
        i += 1
    result = 0
    k = 0
    while k < len(parameters):
        l = 0
        temp = 1  # 分子乘积
        while l < len(parameters):
            if (k != l):
                temp *= new_x - data_x[l]
            l += 1
        result += temp * parameters[k]
        k += 1
    return result  # 返回结果y，描点用

def Draw(origin_data_x, origin_data_y):
    for ndot in (3, 5, 11, 51, 101):  # 点个数
        x = np.linspace(-5, 5, ndot)
        y = []
        for t in x:
            result = 1 / (1 + t ** 2)
            y.append(result)
        x_new = np.linspace(-5, 5, 1001)
        y_new = []
        # 计算拉格朗日插值
        for t in x_new:
            y_new.append(Lagrange(x, y, ndot, t))
        plt.plot(x_new, y_new, label="n=" + str(ndot))  # 插值多项式图像
    plt.plot(origin_data_x, origin_data_y, label="f(x)")  # 原函数图像
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis([-5, 5, -0.5, 1.5])
    plt.legend()
    plt.show()

# 原函数描点
x_origin = np.linspace(-5, 5, 1001)
y_origin = []
for t in x_origin:
    result = 1 / (1 + t ** 2)
    y_origin.append(result)

Draw(x_origin, y_origin)