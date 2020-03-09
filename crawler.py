# %%
import pandas as pd
import time
from tqdm import tqdm

# 比價王網址
url = 'https://price.houseprice.tw/list/?p='

'''
比價王換頁時是靠修改'?p='後的數字來取得不同頁面的資料
所以不需要使用selenium，以靜態爬蟲的方式處理即可
'''


def cralwer(page):
    html = url + str(page)
    page_data = pd.read_html(html, encoding='utf-8')[0]
    # pandas可以直接讀取html格式中的<table>標籤，無需使用Beautifulsoup解析
    return page_data


all_data = pd.DataFrame()   # 建立空白的資料表，再循環加入每一頁的資料

for p in tqdm(range(1, 3)):  
    # range是頁面範圍，請自行修改頁面範圍，程式中斷時也可從修改頁面從中斷的頁面開始
    all_data = all_data.append(cralwer(p), ignore_index=True)

# %%
# 資料輸出
all_data.to_excel('all_data.xlsx')
