#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 #  @file       py_test.py
 #  @brief      
 #  @version    1.0.0
 #  @author     LindenTao(lindentao@qq.com)
 #  @date       17/10/24 上午11:50
 #  @history    <author>    <time>    <desc>
 
"""


from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from base64 import decodebytes, encodebytes

app_private_key = '''-----BEGIN PRIVATE KEY-----
MIIEogIBAAKCAQEAwkho8A1Sdu+kv9TygLYBrar7fLoPKStcBbD+qaukKHW8XQAI4zVO/8VGreQBgaL+OG3HfJ7sd5nJlc62HeWW29/tOSrNNQonA7XDZ/o/2xWWl5UcfEC7E4hORmpyXBqdYgz413jAJSBrP+5ORkXmo6LgIub7DMNruZqEUFlV3THzVjPXBc0ip3qOY6EQjMWOvdNc6H/ENp0fXMpkVKHKgdBubAZexBmMnFfO3mbpHXOfnlwbu4oBIWlNmVpHta4uIYL04pBuaJT8+k8vHGoUrmICzQJYjQesZDl1aQE/hRTB+DgQHRFIKkjTamY9ozycU5+/R0ZgtGiXxVHC08otEwIDAQABAoIBAGVSpD/FguN6eb5+DXbo9RkgmgXjdzKuZVCmjTnpxTRAqtsJwJjWXXvw47qetdZpLhI51pb8vzBk6QgTBVG0Qigrsall1B28TLqXmfBpR9I3gRFO98spayd1p/T7YOb+DmRrhX/Cftsd/DEcVIA7xlxC/ofVVMrERDNJDYZmAOzZTcbquWQzKtqEwJ7QXlIh7VHxLP1v3BMX5QeU8AnmnX4VA2c7jGhNcla8AVZHjKTdGfdxtjybQRYuuVMiaODtyQOOUSUMOV9jw1X+cFUIomdyRimfVzTohfNPPoo3i7g9RbWNt2bA1gZETVq69qzluVIzCqpN62bvnP8aTNdtdYkCgYEA8Xoj6cJv8P8g/f6DGMES+nCdFAJRYmBcMTnfJ/SGdJhChZzAeYmO+DnloJAmBhkMJ4sazk7zHmdJ94Dir9cuv4HSvbnBvL3OtgNHSkVKSvhycn/Rck7lDRNOgWl8OFYpm9m5czd1jMWzoROU8z6dBOSzUWGjwLFPQv9hYR5dPrcCgYEAzfemy48Nt6fbxNAoDGeEakiniKRK/1+/VnIeQMAyxM+sM+cAa8t1YrtspS87FxHIftl8vswwFJtmYeiIhT8bJjNbuScauqhvxwm2aHF2gtjub4THInmq6Tp73OVEQVRgQU8dyGNAPlq7JModq50xNceOp9/VaMg2biLq2NTUKIUCgYBMNVreLEH90dbMsiUXi998cEvyg6TBol2WH4iA6JgCdgcQed74vGQFjOgeWz/UztTaKfmEwL/TiY97cA6aphOX1tX2kIhHE7QIF1LJasK+lFgyMIqeQ63gCYbOKsdMVEz/ZaA0b31GtyIwpKhueAVABRlehq0SZCL6pvRJnTaaUwKBgDg/zBOHi+1+MCy91FIe6zDDis1sYPcBRRXssIpqcvMA7Dx4d8r4k6RVH0S1c2PHfYP3DXRl+zOFhR50DOSm6VkzaXdVUJ1tZqlq45/+bKkraWKXVnL52006pZ0cF9nnmyn6211gjaj5ymYvtI6rrUbMqw75uCSXmRXW/2AcL5ypAoGAfnvDfUp+9Y5HcFi1jwuqu7VZAGcqsBLtv8qbKQEs8JVARA85Xh5dSW3X0RYmrA812PxfALKRDKjoacs/1/GF7O988xYLbc7e+/JhNaaauNfrPMr8A8yLvLyC0oX68aH7J2Yc9K0M2glF7PosAmJiA7098hem+s+sJNcGfYE6L4E=
-----END PRIVATE KEY-----
'''
biz_content = '''{"button": [{"actionParam": "ZFB_HFCZ", "actionType": "out", "name": "话费充值"},
                          {"name": "查询", "subButton": [
                              {"actionParam": "ZFB_YECX", "actionType": "out", "name": "余额查询"},
                              {"actionParam": "ZFB_LLCX", "actionType": "out", "name": "流量查询"},
                              {"actionParam": "ZFB_HFCX", "actionType": "out", "name": "话费查询"}]},
                          {"actionParam": "http://m.alipay.com", "actionType": "link", "name": "最新优惠"}]}'''

sign = 'e9zEAe4TTQ4LPLQvETPoLGXTiURcxiAKfMVQ6Hrrsx2hmyIEGvSfAQzbLxHrhyZ48wOJXTsD4FPnt+YGdK57+fP1BCbf9rIVycfjhYCqlFhbTu9pFnZgT55W+xbAFb9y7vL0MyAxwXUXvZtQVqEwW7pURtKilbcBTEW7TAxzgro='


data = {
    "app_id": 2014072300007148,
    "method": 'alipay.mobile.public.menu.add',
    "charset": "GBK",
    "sign_type": "RSA2",
    "timestamp": '2014-07-24 03:07:50',
    "version": "1.0",
    "biz_content": biz_content,
    "sign": sign,
}

# 筛选、排序、拼接成待签名字符串
unsigned_string = "&".join("{0}={1}".format(k, data[k]) for k in sorted(data) if k != 'sign' and data[k])
print(unsigned_string)


def sign(unsigned_string):
    # 开始计算签名
    key = app_private_key
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(SHA256.new(unsigned_string))
    # base64 编码，转换为unicode表示并移除回车
    sign = encodebytes(signature).decode("utf8").replace("\n", "")
    return sign

sign = sign(unsigned_string.encode("utf-8"))
print(type(sign), sign)


