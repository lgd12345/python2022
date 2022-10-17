import pymysql
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 데이터 베이스 연결 : connect()
# 데이터 베이스 작업을 전달하기 위한 객체 생성:cursor()
# 질의문 전달:execute()
# 실행 : commit()
# select한결과를 가져옴 하나값 fetchone(),여러개값 fetchall()


dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "1234"
conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser, passwd=dbPass,
                       db='BigData', charset='utf8', use_unicode=True)

# 그래프 그리기
font_path = 'c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
matplotlib.rc('font', family=font_name)

# 서울 날씨
select_data = "select * from forecast where city='서울' order by tmef desc"

cur = conn.cursor()
cur.execute(select_data)
result = cur.fetchall()

# 여기에 담김
high = []
low = []
xdata = []
whState = []

# 데이터에서 뽑아서 담을 때 사용 되는 문장
for row in result:
    high.append(float(row[5]))  # 최고기온
    low.append(float(row[4]))  # 최저기온
    whState.append(row[3])  # 날씨 상태
    xdata.append(row[2].split('-')[2])  # 가로축

# 그래프 그리기
plt.figure(figsize=(15, 6))  # 그래프크기
plt.plot(xdata, low, label='최저기온')
plt.plot(xdata, high, label='최고기온')
plt.title(result[0][2].split('-')[1]+"월")  # 타이틀 10월이라는 글자 뽑아서 쓴다.

plt.legend()
plt.show()

# wf
select_data1 = "select wf, count(*) from forecast where city='서울'group by wf;"

# bar
cur.execute(select_data1)
result1 = cur.fetchall()
whData = []
whDataCount = []
for row in result1:
    whData.append(row[0])
    whDataCount.append(row[1])

plt.bar(whData, whDataCount)
plt.show()

# pie
plt.pie(whDataCount, labels=whData, autopct='%.1f%%')
plt.show()
