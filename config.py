#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 #  @file       config.py
 #  @brief      
 #  @version    1.0.0
 #  @author     LindenTao(lindentao@qq.com)
 #  @date       17/10/24 下午7:08
 #  @history    <author>    <time>    <desc>
 
"""


# 我方私钥
private_key = '''-----BEGIN PRIVATE KEY-----
MIIEogIBAAKCAQEAwkho8A1Sdu+kv9TygLYBrar7fLoPKStcBbD+qaukKHW8XQAI4zVO/8VGreQBgaL+OG3HfJ7sd5nJlc62HeWW29/tOSrNNQonA7XDZ/o/2xWWl5UcfEC7E4hORmpyXBqdYgz413jAJSBrP+5ORkXmo6LgIub7DMNruZqEUFlV3THzVjPXBc0ip3qOY6EQjMWOvdNc6H/ENp0fXMpkVKHKgdBubAZexBmMnFfO3mbpHXOfnlwbu4oBIWlNmVpHta4uIYL04pBuaJT8+k8vHGoUrmICzQJYjQesZDl1aQE/hRTB+DgQHRFIKkjTamY9ozycU5+/R0ZgtGiXxVHC08otEwIDAQABAoIBAGVSpD/FguN6eb5+DXbo9RkgmgXjdzKuZVCmjTnpxTRAqtsJwJjWXXvw47qetdZpLhI51pb8vzBk6QgTBVG0Qigrsall1B28TLqXmfBpR9I3gRFO98spayd1p/T7YOb+DmRrhX/Cftsd/DEcVIA7xlxC/ofVVMrERDNJDYZmAOzZTcbquWQzKtqEwJ7QXlIh7VHxLP1v3BMX5QeU8AnmnX4VA2c7jGhNcla8AVZHjKTdGfdxtjybQRYuuVMiaODtyQOOUSUMOV9jw1X+cFUIomdyRimfVzTohfNPPoo3i7g9RbWNt2bA1gZETVq69qzluVIzCqpN62bvnP8aTNdtdYkCgYEA8Xoj6cJv8P8g/f6DGMES+nCdFAJRYmBcMTnfJ/SGdJhChZzAeYmO+DnloJAmBhkMJ4sazk7zHmdJ94Dir9cuv4HSvbnBvL3OtgNHSkVKSvhycn/Rck7lDRNOgWl8OFYpm9m5czd1jMWzoROU8z6dBOSzUWGjwLFPQv9hYR5dPrcCgYEAzfemy48Nt6fbxNAoDGeEakiniKRK/1+/VnIeQMAyxM+sM+cAa8t1YrtspS87FxHIftl8vswwFJtmYeiIhT8bJjNbuScauqhvxwm2aHF2gtjub4THInmq6Tp73OVEQVRgQU8dyGNAPlq7JModq50xNceOp9/VaMg2biLq2NTUKIUCgYBMNVreLEH90dbMsiUXi998cEvyg6TBol2WH4iA6JgCdgcQed74vGQFjOgeWz/UztTaKfmEwL/TiY97cA6aphOX1tX2kIhHE7QIF1LJasK+lFgyMIqeQ63gCYbOKsdMVEz/ZaA0b31GtyIwpKhueAVABRlehq0SZCL6pvRJnTaaUwKBgDg/zBOHi+1+MCy91FIe6zDDis1sYPcBRRXssIpqcvMA7Dx4d8r4k6RVH0S1c2PHfYP3DXRl+zOFhR50DOSm6VkzaXdVUJ1tZqlq45/+bKkraWKXVnL52006pZ0cF9nnmyn6211gjaj5ymYvtI6rrUbMqw75uCSXmRXW/2AcL5ypAoGAfnvDfUp+9Y5HcFi1jwuqu7VZAGcqsBLtv8qbKQEs8JVARA85Xh5dSW3X0RYmrA812PxfALKRDKjoacs/1/GF7O988xYLbc7e+/JhNaaauNfrPMr8A8yLvLyC0oX68aH7J2Yc9K0M2glF7PosAmJiA7098hem+s+sJNcGfYE6L4E=
-----END PRIVATE KEY-----'''

# 支付宝公钥,验证支付宝回传消息使用
public_key = '''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1wmFKmXBSwy5ENmV9CRIc/a0mxrAymj29u10xKC1gXhzwoQxAvHNIn7DwFjRw5E8fkTSc/PLNP/a9YqL6ubLnK2gkKJQEfWyu7HpdVMwYrS9zTePVup8r8wg9GoURluWsxN/3HdhrUpL9KXP9ydMIpos5BdDv2EBEO+ba4bfx1CLpt3ucuU5AjF5FvLD3+x1Npznw71sxEzA97HWQtVZAISz+fuouInFyvBs5+WniHSo/WLmqzvZVL5wBF6garEJ8/dyXZpTL2hg4HHvdJAW8oTaRx3MfVMy6aSS+pe40gH8iTIZpHYs9Oi6gJuu4L4hgK4WFZfUsScws6V4DAsoNQIDAQAB
-----END PUBLIC KEY-----'''

# 支付宝同步返回地址，HTTP/HTTPS开头字符串
return_url = 'http://14.215.135.16:60600/flow/alipayr'
# 支付宝服务器主动通知商户服务器里指定的页面http/https路径
notify_url = 'http://14.215.135.16:60600/flow/alipayn'

