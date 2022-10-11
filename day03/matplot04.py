import matplotlib.pyplot as plt
import pandas as pd


df = pd.DataFrame(
    [[500, 450, 520, 610], [690, 700, 820, 900], [1100, 1030, 1200, 1350], [
        1500, 1030, 1200, 1350], [1550, 1030, 1200, 1350], [1900, 1030, 1200, 1350]],
    index=['2015', '2016', '2017', '2018', '2019', '2020'],
    columns=['first', 'second', 'third', 'fourth']
)

df = df.transpose()  # x축 y축 바꾸기
df.plot()
plt.show()
