import korean_font
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
df[df['가격'].median() ]


#     가. 평균 가격 계산
#     나. 최고 가격 계산
#     다. 최저 가격 계산
#   2. 출판년도 분석
#     가. 연도별 도서 수 계산
