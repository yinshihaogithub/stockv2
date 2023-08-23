from wencai import wencai
import pandas as pd
from util import dingding, money_transfer
import datetime

msg = '# 上一个交易日非一字涨停，今日集合竞价成交量/上一个交易日成交量＞0.09，非st，开盘竞价涨幅＞0％，集合竞价成交额＞1000万，非st，昨日开板次数大于1 \r\n'
query = '上一个交易日非一字涨停，今日集合竞价成交量/上一个交易日成交量＞0.09，非st，开盘竞价涨幅＞0％，集合竞价成交额＞1000万，非st，昨日开板次数大于1，今日竞价涨幅，所属同花顺行业，a股流通市值'

res = wencai.get(query=query)


current_datetime = datetime.datetime.now()
current_datetime_2 = (datetime.datetime.now() - datetime.timedelta(days=1))

dayOfWeek = current_datetime.isoweekday()
if dayOfWeek == 1:
    current_datetime_2 = (current_datetime_2 - datetime.timedelta(days=2))
elif dayOfWeek == 6:
    current_datetime = (current_datetime - datetime.timedelta(days=1))
elif dayOfWeek == 7:
    current_datetime = (current_datetime - datetime.timedelta(days=2))
datetime_format = current_datetime.strftime("%Y%m%d")
datetime_format_2 = current_datetime_2.strftime("%Y%m%d")

print(datetime_format)
print(datetime_format_2)

for i in res:
    print(i)

    stock_code = i['股票简称']
    time_sharing = i['竞价涨幅[' + datetime_format + ']']
    try:
        market_value = i['a股市值(不含限售股)[' + datetime_format + ']']
    except Exception:
        try:
            market_value = i['a股市值(不含限售股)[' + datetime_format_2 + ']']
        except Exception:
            market_value = 0
    msg += '<font color=#0000FF	>' + stock_code + '</font>' + ' \r\n - 分时涨跌幅：<font color=FF0000>' \
               + "%.2f" % float(time_sharing) + '</font>' + \
               '\r\n - 流通市值：' + money_transfer.humanize_float_cn(float(market_value)) + \
               '\r\n\r\n'

dingding.send_report_markdown(msg)

