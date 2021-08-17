from yoppy-test.yoppy_lambda.BatchProcessing import handle_date,export_csv
import pandas as pd
from datetime import datetime, timedelta, timezone
def test_handle_date():
    x=handle_date()

    JST = timezone(timedelta(hours=+9), 'JST')
    today = datetime.now(JST)
    lastmonth = datetime(today.year, today.month-1,1)
    global a0    
    a0=lastmonth.strftime("%Y-%m")
    global a1
    a1='/tmp/yoppylog'
    a2='monthly/latest/yoppylog'
    a3=lastmonth.strftime("%Y")+'/'+lastmonth.strftime("%m")+'/yoppylog'
    assert x[0]==a0 #'2021-07'
    assert x[1]==a1#'/tmp/yoppylog'
    assert x[2]==a2#'monthly/latest/yoppylog'
    assert x[3]==a3#'2021/07/yoppylog'


def test_export_csv():
    #仮データ
    response={'Count': 2,'Items': [{'mail_address': 'okuhara@arara.com','reservation_num': 3,'used_at_date': '2021-07-31','used_in': 'Happy食堂'},{'mail_address': 'tamagawa@arara.com','reservation_num': 1,'used_at_date': '2021-07-31','used_in': 'Happy食堂'}],'ResponseMetadata': {'HTTPHeaders': {'connection': 'keep-alive','content-length': '309','content-type': 'application/x-amz-json-1.0','date': 'Fri, 13 Aug 2021 06:51:55 GMT','server': 'Server','x-amz-crc32': '111695128','x-amzn-requestid': '9LAFQD1E1TBD8NDAOJF9M3VL5BVV4KQNSO5AEMVJF66Q9ASUAAJG'},'HTTPStatusCode': 200,'RequestId': '9LAFQD1E1TBD8NDAOJF9M3VL5BVV4KQNSO5AEMVJF66Q9ASUAAJG','RetryAttempts': 0},'ScannedCount': 8}
    export_csv(response['Items'],a1)

    test_frame=pd.read_csv(a1)  #csvファイルかどうかはここでわかる
    assert not test_frame.isnull().values.sum() #csvにnullがないことを確認
    date_list=test_frame.利用日.tolist()
    for x in date_list:
        assert x.startswith(a0)  #csv内の利用日項目が指定した年月のものだけであること