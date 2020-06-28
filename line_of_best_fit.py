# coding=UTF-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def draw_linear_regression(x, y):
    linear = LinearRegression()
    x_array = np.array(x)
    y_array = np.array(y)
    xfit = x_array.reshape(-1, 1)
    yfit = y_array.reshape(-1, 1)

    linear.fit(xfit, yfit)
    xpre = np.linspace(0, 82, num=50, endpoint=True)  # 创建用于预测的x值
    ypre = linear.predict(xpre[:, np.newaxis])

    plt.plot(xpre, ypre, "-", label="degree 1")



def draw_poly_feature(x, y):
    # translate list type to array
    x_array = np.array(x)
    y_array = np.array(y)
    xfit = x_array.reshape(-1, 1)
    yfit = y_array.reshape(-1, 1)
    xpre = np.linspace(0, 82, num=50, endpoint=True)  # 创建用于预测的x值

    # three and four degrees are closest
    for i in [3,4]:
        PF = PolynomialFeatures(degree=i)
        xfit1 = PF.fit_transform(xfit)
        linear1 = LinearRegression()
        linear1.fit(xfit1, yfit)
        xpre1 = PF.fit_transform(xpre[:, np.newaxis])
        ypre1 = linear1.predict(xpre1)
        plt.plot(xpre, ypre1, "-", label="degree {}".format(i))
