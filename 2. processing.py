import korean_font
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(
    './data_out.csv' ,
    header=0,
    encoding='utf-8'
)

# 쉼표(,) 제거 및 "원" 문자열 제거
df["가격"] = df["가격"].str.replace(",", "").astype(int)
# 출판년월 데이터 전처리
df['출판년월'] = pd.to_datetime(df['출판년월'], format='%Y년 %m월')
df['연도'] = df['출판년월'].dt.year
df['월'] = df['출판년월'].dt.month
print(df['연도'].head)
print(df['월'].head)

# 1. 가격 통계 분석
#     가. 평균 가격 계산
#     나. 최고 가격 계산
#     다. 최저 가격 계산
#   2. 출판년도 분석
#     가. 연도별 도서 수 계산
print( "평균가", df['가격'].mean())
print( "최고가", df['가격'].max())
print( "최저가", df['가격'].min())
print( df['연도'].value_counts())

# 4. 데이터 시각화 기능
#   1. 가격 분포 시각화
#     가. 히스토그램 구현
#     나. 가격대별 도서 개수 출력
sns.histplot( df[ '가격' ] )
plt.title('가격분포')
plt.xlabel('가격대')
plt.ylabel('도서 수')
plt.legend()
plt.show()

counts, edges = np.histogram(df['가격'], bins = 5)
plt.hist(df['가격'], bins = 5, color ='skyblue')
plt.title('가격대별 도서 개수')
plt.xlabel('가격')
plt.ylabel("도서 개수")
plt.show()