# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 16:52
# @Author  : ZhuNian
# @FileName: course_13_2.py
# @Software: PyCharm

#python 原生爬虫
'''
1.模拟HTTP请求
2.断点调试
3.HTML结构分析基本原则两条
'''

import re
from urllib import request  #模拟HTTP请求
from io import BytesIO
import gzip
#用url抓取网页地址

class Spider():
    '''
    url为网页地址，root_patter、name_pattern、number_pattern为获取信息的正则表达式规则
    '''
    url = 'https://www.douyu.com/g_jdqs'
    root_pattern = '<div class="DyListCover-info">([\s\S]*?)</div>'  #[\s\S]*? 无穷字符非贪婪（用于匹配一个标签下的值。加上（）获取组
    name_pattern = '</svg>([\s\S]*?)</svg>([\s\S]*?)</h2>'  #获取名字
    number_pattern = '</svg>([\s\S]*?)</span>'  #获取人气数

    def __fetch_content(self):
        '''
        将字节码转换成 HTML 文本格式
        '''
        r = request.urlopen(Spider.url) #抓取网页地址
        htmls = r.read()  # bytes格式  读取网页信息

        #将字节码转换成 HTML 文本格式
        buff = BytesIO(htmls)
        f = gzip.GzipFile(fileobj=buff)
        htmls = f.read().decode('utf-8')  #将字节码转换成 HTML 文本格式  #可以在谷歌浏览器中网页下右键找《查看网页源码》

        return htmls

    def __analysis(self,htmls):
        '''
        通过正则表达式，过去具体名字、人气值的数据
        '''
        root_html = re.findall(Spider.root_pattern,htmls)#print(root_html[1])

        #循环进行正则匹配
        n = 1
        length = len(root_html)   #print(length)
        anchors = []
        for html in root_html:
            if n%2 == 0 :
                name = re.findall(Spider.name_pattern, html)
                name = name[0][1]
                number = re.findall(Spider.number_pattern, html)
                anchor = {'name': name, 'number': number}
                anchors.append(anchor)
            else:
                pass
            n += 1
        return anchors


    def __refine(self,anchors):
        '''
        #过滤掉多余的空格
        #定义一个lambda表达式：
        '''
        func = lambda anchor: {'name':anchor['name'],
                             'number':anchor['number'][0]}  #strip()用于去除字符串空格
        return map(func,anchors)

    def __sort(self, anchors_list):
        '''
        按照anchor['number']的值进行排序
        '''
        anchors_list = sorted(anchors_list, key = self.__sort_number, reverse= True)
        return anchors_list

    def __sort_number(self, anchor):
        return anchor['number']

    def __sort_seed(self, anchors):
        '''
        将字符串换成 浮点类型的数据，并将‘万’ 改成浮点类型数据进行比较
        作为__sort的种子，返回具有 （anchor['number']：整型）的值
        '''
        anchors_sort = []
        for anchor in anchors:
            numeber_wan = self.__sort_number(anchor)
            if '万' in numeber_wan:
                r = re.findall('[0-9.]', numeber_wan)
                r_new = ''.join([str(i) for i in r])
                number_new = float(r_new) * 10000
                anchor['number'] = int(number_new)
                anchors_sort.append(anchor)
            else:
                number_new = numeber_wan
                anchor['number'] = int(number_new)
                anchors_sort.append(anchor)

        return anchors_sort


    # 展示列表
    def __show(self, anchors):
        '''
        # 展示列表
        '''
        for rank in range(0, len(anchors)):
           print(' rank ', rank +1,
                 ' : ',anchors[rank]['name'],
                 ' : ',anchors[rank]['number'])



    def go(self):
        '''
        Spider的入口方法
        '''
        htmls = self.__fetch_content()  #返回  HTML文本格式的 列表字符串
        anchors = self.__analysis(htmls)  #返回 含有 名字 和 人气值 的列表
        anchors_list = self.__refine(anchors)  #返回 过滤掉多余的空格 的列表
        anchors_list = self.__sort_seed(anchors_list)  #返回 过滤掉多余的空格 的列表
        r_new = self.__sort(anchors_list)  #返回 过滤掉多余的空格 的列表
        self.__show(r_new)


spider = Spider()
spider.go()



