import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

#  인코딩이 utf-8이면 실행이 안 됨..
df = pd.read_csv('weather.csv', index_col='point', encoding='euc-kr')
# print(df)

# 서울 인천 부산 데이터 출력
print(df.loc[['서울', '인천', '부산']])
# 서울 인천 대전 대구 광주 부산 울산
city_df = df.loc[['서울', '인천', '대전', '대구', '광주', '부산', '울산']]
print(city_df)

# 그래프 그리기
font_name = mpl.font_manager.FontProperties(
    fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

# 차트종류, 제목, 차트크기,범례,폰트 크기 설정
ax = city_df.plot(kind='bar', title='날씨', figsize=(12, 7),
                  legend=True, fontsize=12)
ax.set_xlabel('도시', fontsize=12)
ax.set_ylabel('기온/습도', fontsize=12)
ax.legend(['기온', '습도'], fontsize=12)
plt.show()
