# reference https://www.w3schools.com/python/matplotlib_intro.asp

import matplotlib.pyplot as plt
import numpy as np




def plot_bar():
    x_points = np.array([1, 2, 6, 8, 10])
    y_points = np.array([3, 8, 1, 10, 12])
    y2_points = y_points + 1

    plt.plot(x_points, y_points)
    plt.plot(x_points, y_points, marker = '*') # plot with markers
    plt.plot(x_points, y_points, linestyle = 'dotted')
    plt.scatter(x_points, y_points)
    plt.scatter(x_points, y2_points, color = '#88c999')

    plt.bar(x_points, y_points)


    plt.title("Sports Watch Data")
    plt.xlabel("Average Pulse")
    plt.ylabel("Calorie Burnage")

    plt.grid()


    plt.show()

# pie chart
def plot_pie():
    y = np.array([35, 25, 25, 15])
    plt.pie(y)
    plt.show()

plot_bar()
# plot_pie()