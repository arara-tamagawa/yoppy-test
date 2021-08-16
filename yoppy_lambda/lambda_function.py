import boto3
from datetime import datetime, timedelta, timezone
from boto3.dynamodb.conditions import Key, Attr
import pandas as pd
import numpy as np

#dynamodb指定
DYNAMO_TABLE_NAME = 'yoppy-test-db2'    #要確認
dynamodb = boto3.resource('dynamodb')
table    = dynamodb.Table(DYNAMO_TABLE_NAME)
#s3指定
s3_resource = boto3.resource('s3')
OUTPUT_BUCKET = 'log-yoppy-csv'         #要確認


def handle_date():
    #日付取得
    JST = timezone(timedelta(hours=+9), 'JST')
    today = datetime.now(JST)
    lastmonth = datetime(today.year, today.month-1,1)
    
    lastmonth_str=lastmonth.strftime("%Y-%m")
    
    year_only_str=lastmonth.strftime("%Y")
    month_only_str=lastmonth.strftime("%m")
    
    TEMP_FILENAME = '/tmp/食堂利用情報_' + year_only_str + '_' + month_only_str + '.csv' #/tmp/のパスが必要
    LATEST_OUTPUT_KEY = 'latest/食堂利用情報_' + year_only_str + '_' + month_only_str + '.csv' #上書きされる
    LAST_MONTH_OUTPUT_KEY =  year_only_str + '/' + month_only_str + '/食堂利用情報_' + year_only_str + '_' + month_only_str + '.csv'   #2021/07/export.csv
    print(TEMP_FILENAME)
    print(LATEST_OUTPUT_KEY)
    print(LAST_MONTH_OUTPUT_KEY)
    return [lastmonth_str,TEMP_FILENAME,LATEST_OUTPUT_KEY,LAST_MONTH_OUTPUT_KEY]

def export_csv(frame,temp_filename):
    #dynamoDBからアイテムを取得
    df = pd.DataFrame(frame)
    #金額とゲスト有無のカラムを追加
    df2 = df.assign(利用金額=lambda x: (x['reservation_num']*200))
    df2 = df2.assign(ゲスト有無=lambda x: np.where((x['reservation_num']>1),'1','0'))
    df2 = df2.rename(columns={'mail_address':'利用者','used_at_date':'利用日','used_in':'利用場所','reservation_num':'利用人数'})
    #確認用
    print(df2.to_string())
    #csvファイルにエクスポート
    data = df2.to_csv(temp_filename, index=False, header=True)
    print(type(data))
    return data

def get_table(year_lastmonth_information):
    options = {
        'FilterExpression': Attr('used_at_date').contains(year_lastmonth_information),
        'ProjectionExpression' : 'mail_address,used_at_date,used_in,reservation_num'
    }
    response = table.scan(**options)
    #確認用
    print('-----------response------------------')
    print(type(response))
    pprint.pprint(response)
    print('-------------------------------------')
    return response

def lambda_handler(event, context):
    url_info=handle_date()
    #csv_file=
    export_csv(get_table(url_info[0])['Items'],url_info[1])
    #s3にアップロード
    s3_resource.Bucket(OUTPUT_BUCKET).upload_file(url_info[1], url_info[2])
    s3_resource.Bucket(OUTPUT_BUCKET).upload_file(url_info[1], url_info[3])
    
    return 0