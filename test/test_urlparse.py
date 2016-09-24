# -*- coding: utf-8 -*-
"""
@Time    : create on 09/24/2016 20:25
@Author  : Alan
@File    : test_urlparse.py
@Software: PyCharm Community Edition
"""
import urlparse

full_url = urlparse.urljoin('http://baike.baidu.com/view/21087.htm', '/view/21.htm')

full_url1 = urlparse.urljoin('http://baike.baidu.com/view/21087.htm', '/view312/21.htm')

print full_url
print full_url1
