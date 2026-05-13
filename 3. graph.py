import korean_font
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(
    './data_out.csv',
    header=0,
    encoding='utf-8'
)
# 1. 가격 통계 분석
#     가. 평균 가격 계산
#     나. 최고 가격 계산
#     다. 최저 가격 계산
#   2. 출판년도 분석
#     가. 연도별 도서 수 계산
print( "평균가", df['가격'].mean())
print( "최고가", df['가격'].max())
print( "최저가", df['가격'].min())
print( df['출판년도'].value_counts())