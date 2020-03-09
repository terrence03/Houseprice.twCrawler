#%%
# -- coding: utf-8 --
import pandas as pd
import time
from tqdm import tqdm

url = 'https://price.houseprice.tw/list/?p='

def cralwer(page):
    html = url + str(page)
    page_data = pd.read_html(html, encoding='utf-8')[0]
    #time.sleep(5)
    return page_data

#data = pd.DataFrame(columns=['成交年月','地址','型態','總價','單價','建坪','地坪','樓別','屋齡','移轉記錄'])
all_data = pd.DataFrame()

for p in tqdm(range(1, 3)):
    all_data = all_data.append(cralwer(p), ignore_index=True)


# %%
