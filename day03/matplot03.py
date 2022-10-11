import matplotlib.pyplot as plt
import pandas as pd


color = ['b', 'orange', 'green', 'red', 'purple', 'brown']
xLabel = ['first', 'second', 'third', 'fourth']

data = pd.DataFrame([[500, 450, 5300, 610],
                     [400, 350, 230, 1010],
                     [500, 450, 530, 610],
                     [400, 3500, 230, 110],
                     [500, 4500, 530, 610],
                     [400, 360, 230, 110]
                     ])
y1 = [500, 450, 5300, 610]
y2 = [400, 350, 230, 1010]
y3 = [500, 450, 530, 610]
y4 = [400, 3500, 230, 110]
y5 = [500, 4500, 530, 610]
y6 = [400, 360, 230, 110]

x = range(len(y1))
plt.plot(x, y1, color='b')
plt.plot(x, y2, color='orange')
plt.plot(x, y3, color='green')
plt.plot(x, y4, color='red')
plt.plot(x, y5, color='purple')
plt.plot(x, y6, color='brown')

plt.title('2015~2022 Quarterly sales')
plt.xlabel('Quarters')
plt.ylabel('sales')
plt.legend(['2015', '2016', '2017', '2018', '2019', '2020'],
           loc='upper left')  # legend:범례
plt.xticks(x, xLabel)  # xticks x축에 표시되는 값

plt.show()
