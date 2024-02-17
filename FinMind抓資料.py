# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 16:25:09 2024

@author: user
"""

# 取得股價
from FinMind.data import DataLoader
import pandas as pd
from datetime import datetime
from os import listdir

catched_stock_list = listdir("FINMIND資料/")

api = DataLoader()
api.login(user_id='nkust_finmind24@gmail.com',
          password='nkust_finmind24@gmail.com')

stock_info = api.taiwan_stock_info() 
# print(stock_info) #若無回傳資料，print看看最後更新日期，更改date=="最後更新日期"
#stock_info.to_excel("stock_info.xlsx")
stock_info = stock_info[(stock_info["date"] == "2024-02-01") &
                        (stock_info["type"] == "twse")]

stock_list = pd.unique(stock_info["stock_id"])

rename_dict = {
    "Trading_Volume" : "Volume",
    "open" : "Open",
    "max" : "High",
    "min" : "Low",
    "close" : "Close",
    }

for s_id in stock_list:
    if (s_id + ".xlsx") in catched_stock_list:
        continue

    # 下載台股股價資料
    stock_data = api.taiwan_stock_daily(
        stock_id=s_id,
        start_date='2018-01-01',
        end_date='2024-01-18'
    )
    stock_data.columns
    if stock_data.shape[0] < 100:
        continue
    print(s_id, datetime.now(), stock_data.shape)
    
    stock_data = stock_data.drop(["stock_id"], axis = 1)
    stock_data = stock_data.rename(columns = rename_dict)

    stock_data.to_excel(f"FINMIND資料/{s_id}.xlsx", index = False)

print("test for git")
print("practice for sourcetree")
print("practice for github")
# =============================================================================
# df = api.taiwan_stock_per_pbr(
#     stock_id='2330',
#     start_date='2020-01-02'
# )
# =============================================================================
#print(stock_data)
# =============================================================================
# # 下載三大法人資料
# stock_data = dl.feature.add_kline_institutional_investors(
#     stock_data
# ) 
# # 下載融資券資料
# stock_data = dl.feature.add_kline_margin_purchase_short_sale(
#     stock_data
# )
# 
# =============================================================================
# =============================================================================
# # 繪製k線圖
# from FinMind import plotting
# 
# plotting.kline(stock_data)
# =============================================================================

