# -*- coding: utf-8 -*-
"""
@Time    : create on 09/24/2016 19:14
@Author  : Alan
@File    : html_outputer.py
@Software: PyCharm Community Edition
"""
import os


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
        self.output_dir = self.create_output_dir()

    def create_output_dir(self):
        output_dir_path = self.full_path('output_dir')
        if os.path.exists(output_dir_path):
            print '目录已存在'
        else:
            os.mkdir(output_dir_path, 0777)
        return output_dir_path

    def collect_data(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)

    def out_html(self, file_name):
        fout = open(os.path.join(self.output_dir, file_name), 'w')

        fout.write('<html>')
        fout.write('<head>')
        fout.write('<meta charset="utf-8" />')
        fout.write('<title>NetSpider powered by Python</title>')
        fout.write('</head>')
        fout.write('<body>')
        fout.write('<table>')

        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'].encode('utf-8'))
            fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()

    def full_path(self, dir_name):
        if dir_name is None or len(dir_name) == 0:
            return
        return os.path.join(os.path.abspath('.'), dir_name)
