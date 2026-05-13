import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
book_list=[]
for page in range(1,9) :
    url = f'https://www.yes24.com/product/category/bestseller?categoryNumber=001&pageNumber=1&pageSize=120'
    response = requests.get( url )
    soup = BeautifulSoup( response.text, 'html.parser' )
    books = soup.select( '#yesBestList > li' )
    for book in books :
        gd_name = book.select_one('.gd_name').get_text().strip() # 책 제목
        yes_b = book.select_one(".yes_b").get_text().strip() # 가격
        saleNum = book.select_one(".saleNum").get_text().strip() # 판매지수
        info_date = book.select_one(".info_date").get_text().strip() # 출판년월
        book_list.append( {"제목" : gd_name, "가격": yes_b, "판매지수": saleNum, "출판년월": info_date })

    df = pd.DataFrame( book_list )
    print( df )

df.to_csv(
    './data_out.csv' ,
    index=False ,
    encoding='utf-8',
    na_rep='Unknown',
    header=True
)