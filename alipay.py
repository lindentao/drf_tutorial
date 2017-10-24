#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 #  @file       alipay.py
 #  @brief      https://docs.open.alipay.com/270/105899
                pip install pycryptodome
 #  @version    1.0.0
 #  @author     LindenTao(lindentao@qq.com)
 #  @date       17/10/23 上午11:32
 #  @history    <author>    <time>    <desc>

"""

import json
from datetime import datetime
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from urllib.parse import quote_plus
from urllib.parse import urlparse, parse_qs
from base64 import decodebytes, encodebytes

import config


class AliPay(object):
    """
    支付宝支付接口
    """
    def __init__(self, app_id, debug=False):
        self.app_id = app_id
        self.charset = 'utf-8'
        self.sign_type = 'RSA2'
        self.version = '1.0'
        self.notify_url = config.notify_url
        self.return_url = config.return_url
        self.app_private_key = RSA.importKey(config.private_key)
        self.alipay_public_key = RSA.import_key(config.public_key)

        if debug is True:
            self.__gateway = "https://openapi.alipaydev.com/gateway.do"
        else:
            self.__gateway = "https://openapi.alipay.com/gateway.do"

    def alipay_trade_page_pay(self, out_trade_no, total_amount, subject, method='alipay.trade.page.pay',
                              product_code='FAST_INSTANT_TRADE_PAY', **kwargs):
        # PC场景下单并支付
        biz_content = {
            "out_trade_no": out_trade_no,
            "total_amount": total_amount,
            "subject": subject,
            "product_code": product_code
        }
        biz_content.update(kwargs)

        params = {
            "app_id": self.app_id,
            "charset": self.charset,
            "sign_type": self.sign_type,
            "version": self.version,
            "method": method,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "biz_content": biz_content
        }
        if self.notify_url:
            params["notify_url"] = self.notify_url
        if self.return_url:
            params["return_url"] = self.return_url

        # params = {
        #     "app_id": '2014072300007148',
        #     "charset": 'GBK',
        #     "sign_type": 'RSA2',
        #     "version": '1.0',
        #     "method": 'alipay.mobile.public.menu.add',
        #     "timestamp": '2014-07-24 03:07:50',
        #     "biz_content": '''{"button":[{"actionParam":"ZFB_HFCZ","actionType":"out","name":"话费充值"},{"name":"查询","subButton":[{"actionParam":"ZFB_YECX","actionType":"out","name":"余额查询"},{"actionParam":"ZFB_LLCX","actionType":"out","name":"流量查询"},{"actionParam":"ZFB_HFCX","actionType":"out","name":"话费查询"}]},{"actionParam":"http://m.alipay.com","actionType":"link","name":"最新优惠"}]}'''
        # }

        return self.sign_data(params)

    def sign_data(self, data):
        # 筛选、排序、拼接成待签名字符串
        data.pop("sign", None)
        # 排序后的字符串
        unsigned_items = self.ordered_data(data)
        unsigned_string = "&".join("{0}={1}".format(k, v) for k, v in unsigned_items)
        sign = self.sign(unsigned_string.encode("utf-8"))
        ordered_items = self.ordered_data(data)
        quoted_string = "&".join("{0}={1}".format(k, quote_plus(v)) for k, v in ordered_items)

        # 获得最终的订单信息字符串
        signed_string = quoted_string + "&sign=" + quote_plus(sign)
        return signed_string

    def ordered_data(self, data):
        complex_keys = []
        for key, value in data.items():
            if isinstance(value, dict):
                complex_keys.append(key)

        # 将字典类型的数据dump出来
        for key in complex_keys:
            data[key] = json.dumps(data[key], separators=(',', ':'))

        return sorted([(k, v) for k, v in data.items()])

    def sign(self, unsigned_string):
        # 开始计算签名
        key = self.app_private_key
        signer = PKCS1_v1_5.new(key)
        signature = signer.sign(SHA256.new(unsigned_string))
        # base64 编码，转换为unicode表示并移除回车
        sign = encodebytes(signature).decode("utf8").replace("\n", "")
        return sign

    def verify(self, data, signature):
        # 验证签名
        message = "&".join("{0}={1}".format(k, data[k]) for k in sorted(data) if k != 'sign_type' and data[k])
        key = self.alipay_public_key
        signer = PKCS1_v1_5.new(key)
        digest = SHA256.new()
        digest.update(message.encode("utf8"))
        if signer.verify(digest, decodebytes(signature.encode("utf8"))):
            return True
        return False


if __name__ == "__main__":
    # post 参数:b'gmt_create=2017-10-24+11%3A24%3A33&charset=utf-8&gmt_payment=2017-10-24+11%3A24%3A41&notify_time=2017-10-24+11%3A24%3A42&subject=%E6%B5%8B%E8%AF%95%E8%AE%A2%E5%8D%95&sign=vhbCTlz2TqXu99b7d6G2MqEEB3U7NnCybVH34lW6CdbXlwmd5lj%2BDxDmkEfkBFGADMNegv9%2FmZNAD%2BrLjNUpj0jHAxxtswzjW9lUYOJQHa0LdoO%2FMI3%2FqFFDzcF8jzr7l6Pi066kRVx43u2iijw77op%2BbGfQLJ9J2AYNhBYUJpB7oaYwmNnYsvAbC%2Fr8dLsUGGvmXud5vPt08jCg2orUF42Z6u2w3CK4HgHTVUsysdReiz3EFvBIaoRzblJIavktycCTzzp1w68KVlgKBbyDK1M%2BG7lZuXvAFc5jbYY6Bh172kUJcBUYFoPPPeRc0sJWK1Q3HiOF%2BasUZSIuKX16cw%3D%3D&buyer_id=2088102174781102&invoice_amount=0.01&version=1.0&notify_id=8b4b9d16cfd30a532ad9dfeeeda3631gru&fund_bill_list=%5B%7B%22amount%22%3A%220.01%22%2C%22fundChannel%22%3A%22ALIPAYACCOUNT%22%7D%5D&notify_type=trade_status_sync&out_trade_no=2017020212231&total_amount=0.01&trade_status=TRADE_SUCCESS&trade_no=2017102421001004100200369973&auth_app_id=2016080800194155&receipt_amount=0.01&point_amount=0.00&app_id=2016080800194155&buyer_pay_amount=0.01&sign_type=RSA2&seller_id=2088102170454992'
    callback_url = 'http://14.215.135.16:60600/flow/alipay?total_amount=0.01&timestamp=2017-10-24+11%3A24%3A49&sign=vVfK7ce7jNwhJGyOp9q1vsx1Vq%2FfokgSZaT4oRuAe3PEmg5q5rwi%2FODpe8kSaWbTGJt9kxAs18GHa8lVQkD1tYCengGNZY2XwBPLSKXc1hKixx4G1Sem%2FcI%2FW1gTkbk4GlPaipSrvJAsou4ATSepgpNogbsm1Hg1A7zo3ik72Q0uXreCEOUOXlL9PIibby8rGAnrkzKxrglp9RZJDjg2DakWunLROBqAd136SkboXfweJmcxLpG%2Bk7F3LBo6B%2Ba9KA%2BdHWr4pAF%2FeQ%2BbBM3JuRX5c3J9BFKL47gOIQGSAmtKgECs5zuy%2BIGTSvEI9Mmmo8iIs7Mx%2B1cPvoW6Any%2F1A%3D%3D&trade_no=2017102421001004100200369973&sign_type=RSA2&auth_app_id=2016080800194155&charset=utf-8&seller_id=2088102170454992&method=alipay.trade.page.pay.return&app_id=2016080800194155&out_trade_no=2017020212231&version=1.0'

    alipay = AliPay(
        app_id="2016080800194155",
        debug=True
    )

    o = urlparse(callback_url)
    query = parse_qs(o.query)
    processed_query = {}
    ali_sign = query.pop("sign")[0]
    for key, value in query.items():
        processed_query[key] = value[0]
    print(alipay.verify(processed_query, ali_sign))

    url = alipay.alipay_trade_page_pay(
        out_trade_no="201702021223122",
        total_amount=0.01,
        subject="测试订单"
    )
    re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)
    print(re_url)
