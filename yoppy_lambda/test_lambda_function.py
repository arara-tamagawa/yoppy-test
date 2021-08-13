from yoppy_lambda.lambda_function import handle_date,export_csv
import pandas as pd
def test_handle_date():
    x=handle_date()
    assert x[0]=='2021-07'
    assert x[1]=='/tmp/食堂利用情報_2021_07.csv'
    assert x[2]=='latest/食堂利用情報_2021_07.csv'
    assert x[3]=='2021/07/食堂利用情報_2021_07.csv'


def test_export_csv():
    response={'Count': 2,'Items': [{'mail_address': 'okuhara@arara.com','reservation_num': 3,'used_at_date': '2021-07-31','used_in': 'Happy食堂'},{'mail_address': 'tamagawa@arara.com','reservation_num': 1,'used_at_date': '2021-07-31','used_in': 'Happy食堂'}],'ResponseMetadata': {'HTTPHeaders': {'connection': 'keep-alive','content-length': '309','content-type': 'application/x-amz-json-1.0','date': 'Fri, 13 Aug 2021 06:51:55 GMT','server': 'Server','x-amz-crc32': '111695128','x-amzn-requestid': '9LAFQD1E1TBD8NDAOJF9M3VL5BVV4KQNSO5AEMVJF66Q9ASUAAJG'},'HTTPStatusCode': 200,'RequestId': '9LAFQD1E1TBD8NDAOJF9M3VL5BVV4KQNSO5AEMVJF66Q9ASUAAJG','RetryAttempts': 0},'ScannedCount': 8}
    print(type(response))
    y=export_csv(response,'/tmp/食堂利用情報_2021_07.csv')
    test_frame=pd.read_csv(y)
    assert not test_frame.df.isnull().values.sum()