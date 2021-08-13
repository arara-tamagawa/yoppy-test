from yoppy_lambda.lambda_function import handle_date

lastmonth_str=''
TEMP_FILENAME=''
LATEST_OUTPUT_KEY=''
LAST_MONTH_OUTPUT_KEY=''

def test_handle_date():
    handle_date()
    assert last_month_str=='2021-07'
    assert TEMP_FILENAME=='/tmp/食堂利用情報_2021_07.csv'
    assert LATEST_OUTPUT_KEY=='latest/食堂利用情報_2021_07.csv'
    assert LAST_MONTH_OUTPUT_KEY=='2021/07/食堂利用情報_2021_07.csv'

"""
def test_export_csv():
    response={'Count': 2,
'Items': [{'mail_address': 'okuhara@arara.com',
'reservation_num': 3,
'used_at_date': '2021-07-31',
'used_in': 'Happy食堂'},
{'mail_address': 'tamagawa@arara.com',
'reservation_num': 1,
'used_at_date': '2021-07-31',
'used_in': 'Happy食堂'}],
'ResponseMetadata': {'HTTPHeaders': {'connection': 'keep-alive',
'content-length': '309',
'content-type': 'application/x-amz-json-1.0',
'date': 'Fri, 13 Aug 2021 06:51:55 GMT',
'server': 'Server',
'x-amz-crc32': '111695128',
'x-amzn-requestid': '9LAFQD1E1TBD8NDAOJF9M3VL5BVV4KQNSO5AEMVJF66Q9ASUAAJG'},
'HTTPStatusCode': 200,
'RequestId': '9LAFQD1E1TBD8NDAOJF9M3VL5BVV4KQNSO5AEMVJF66Q9ASUAAJG',
'RetryAttempts': 0},
'ScannedCount': 8}
"""