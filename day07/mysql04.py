import pymysql
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager, rc

dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "1234"
conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser, passwd=dbPass,
                       db='BigData', charset='utf8', use_unicode=True, cursorclass=pymysql.cursors.DictCursor)
# 그래프 그리기
font_path = 'c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
matplotlib.rc('font', family=font_name)

# 서울 날씨
select_data = "select * from forecast where city='서울' order by tmef desc"

cur = conn.cursor()
cur.execute(select_data)
result = cur.fetchall()

df = pd.DataFrame(result)
print(df)

plt.plot(pd.to_numeric((df['tmn'])),  label='최저기온')
plt.plot(pd.to_numeric((df['tmax'])),  label='최고기온')
plt.legend()
plt.show()

# cursorclass=pymysql.cursors.DictCursor 이거 안 해줄 때
# plt.plot(pd.to_numeric((df[4])),  label='최저기온')
# plt.plot(pd.to_numeric((df[5])),  label='최고기온')
