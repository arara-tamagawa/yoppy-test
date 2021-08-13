from datetime import datetime, timedelta, timezone
import pandas as pd
import numpy as np


def handle_date():
    #日付取得
    JST = timezone(timedelta(hours=+9), 'JST')
    today = datetime.now(JST)
    lastmonth = datetime(today.year, today.month-1,1)
    
    global lastmonth_str
    lastmonth_str=lastmonth.strftime("%Y-%m")
    
    year_only_str=lastmonth.strftime("%Y")
    month_only_str=lastmonth.strftime("%m")
    
    global TEMP_FILENAME
    TEMP_FILENAME = '/tmp/食堂利用情報_' + year_only_str + '_' + month_only_str + '.csv' #/tmp/のパスが必要
    global LATEST_OUTPUT_KEY 
    LATEST_OUTPUT_KEY = 'latest/食堂利用情報_' + year_only_str + '_' + month_only_str + '.csv' #上書きされる
    global LAST_MONTH_OUTPUT_KEY 
    LAST_MONTH_OUTPUT_KEY =  year_only_str + '/' + month_only_str + '/食堂利用情報_' + year_only_str + '_' + month_only_str + '.csv'   #2021/07/export.csv


def export_csv(f):
    #dynamoDBからアイテムを取得
    df = pd.DataFrame(f)
    #金額とゲスト有無のカラムを追加
    df2 = df.assign(利用金額=lambda x: (x['reservation_num']*200))
    df2 = df2.assign(ゲスト有無=lambda x: np.where((x['reservation_num']>1),'1','0'))
    df2 = df2.rename(columns={'mail_address':'利用者','used_at_date':'利用日','used_in':'利用場所','reservation_num':'利用人数'})
    #確認用
    #print(df2.to_string())
    #csvファイルにエクスポート
    data = df2.to_csv(TEMP_FILENAME, index=False, header=True)
    return data
