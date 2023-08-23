import requests
import json
import hmac
import hashlib
import base64
import urllib.parse
import time


def sign():
    timestamp = str(round(time.time() * 1000))
    secret = 'SEC0b0b3521eebf255335d89bb9164825f0861cc2e11086dc4481b8a3974b69da00'
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    print(timestamp)
    print(sign)
    return '&timestamp=' + timestamp + '&sign=' + sign

def send_report_text(msg):
    """
    将报告发送到钉钉群，msg为发送的消息体
    """

    headers = {'Content-Type': 'application/json'}
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=eda93e47d98bd87cbffb0f2ac8f618385aa3db2be5c066c17779f33e99b83b3d' + sign()
    data = {
        "msgtype": "text",
        "text": {
            "content": msg
        }
    }
    r = requests.post(webhook, headers=headers, data=json.dumps(data))
    res = json.loads(r.text)
    print(res)


def send_report_markdown(text):
    """
    将报告发送到钉钉群，msg为发送的消息体
    """

    headers = {'Content-Type': 'application/json'}
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=eda93e47d98bd87cbffb0f2ac8f618385aa3db2be5c066c17779f33e99b83b3d' + sign()
    print(webhook)
    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": "反包公式",
            "text": text
        }
    }
    r = requests.post(webhook, headers=headers, data=json.dumps(data))
    res = json.loads(r.text)
    print(res)