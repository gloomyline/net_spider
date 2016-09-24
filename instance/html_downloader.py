# -*- coding: utf-8 -*-
"""
@Time    : create on 09/24/2016 19:14
@Author  : Alan
@File    : html_downloader.py
@Software: PyCharm Community Edition
"""
import urllib2


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        response = urllib2.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()
