# -*- coding: utf-8 -*-
"""
@Time    : create on 09/24/2016 19:13
@Author  : Alan
@File    : spider_main.py
@Software: PyCharm Community Edition
"""
from instance import html_downloader
from instance import html_outputer
from instance import html_parser
from instance import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        self.outputer.create_output_dir()
        self.urls.add_new_url(root_url)
        count = 1
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %s : %s' % (count, new_url)
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 10:
                    break

                count = count + 1
            except:
                print 'craw failed'

        self.outputer.out_html('output1.html')


if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/view/21087.htm'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
