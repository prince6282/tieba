# -*- coding: utf-8 -*-
import requests
import time
from bs4 import BeautifulSoup

import io
import sys
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gbk') #改变标准输出的默认编码
#生活大爆炸吧
'''
 # 标题&帖子链接：
    <a rel="noreferrer" href="/p/4788526595" title="我的人物设计和制作" target="_blank" class="j_th_tit ">我的人物设计和制作</a>
    
#发帖人：
    <span class="tb_icon_author " title="主题作者: 新日落" data-field="{"user_id":2137596235}"><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer" data-field="{"un":"\u65b0\u65e5\u843d"}" class="frs-author-name j_user_card " href="/home/main/?un=%E6%96%B0%E6%97%A5%E8%90%BD&ie=utf-8&fr=frs" target="_blank">新日落</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
#发帖日期：
  <span class="pull-right is_show_create_time" title="创建时间">2016-09</span>
  
  
#回复数量：
    <div class="col2_left j_threadlist_li_left">
<span class="threadlist_rep_num center_text" title="回复">73</span>
    </div>
'''
#抓取网页的通用框架,获取页面的内容
def getHtml(url):
    try:
        r= requests.get(url,timeout=30)
        #状态码不是200就发出httpError的异常
        r.raise_for_status()
        #获取正确的编码格式
        # r.encoding=r.apparent_encoding
        r.encoding="utf-8"
        #打印内容
        return r.text


    except:
        return "wrong!"



#分析网页的html文件，整理信息，保存问列表文件中
def get_content(url):
    #初始化一个列表来保存所有的帖子信息
    contents=[]

    #获取网页的内容
    html=getHtml(url)

    #将网页内容格式化利用bs4库
    soup = BeautifulSoup(html, 'lxml')

    #获取所有的li标签属性为 j_thread_list clearfix，用列表接收
    liTags = soup.find_all('li', attrs={'class': ' j_thread_list clearfix'})
    print  (len(liTags))

    #循环这个内容li集合
    for li in liTags:

        #将爬取到了每一条信息。保存到字典里
        content={}

        #将异样抛出，避免无数据时，停止运
        try:
            #开始筛选信息
            content['title']=li.find('a',attrs={"class":"j_th_tit"}).text.strip()#.strip()  翻译为中文
            print (li.find('a',attrs={"class":"j_th_tit"}).text.strip())

            #获取a标签的内部属性
            content['link'] ="http://tieba.baidu.com/"+li.find('a', attrs={"class": "j_th_tit"})["href"]
            print("http://tieba.baidu.com/"+li.find('a', attrs={"class": "j_th_tit"})["href"])


            content['author']=li.find('span',attrs={"class":'tb_icon_author '}).text.strip()
            print (li.find('span',attrs={"class":'tb_icon_author '}).text.strip())


            content['responseNum']=li.find('span',attrs={'class': 'threadlist_rep_num center_text'}).text.strip()
            print(li.find(
                'span', attrs={'class': 'threadlist_rep_num center_text'}).text.strip())
            content['creatTime']=li.find('span',attrs={"class":'pull-right is_show_create_time'}).text.strip()
            print (li.find(
                'span', attrs={'class': 'pull-right is_show_create_time'}).text.strip())
            #将字典加入到列表中
            contents.append(content)


        except:
            print('出问题')



        #返回数据
    return contents


def writeTxt(content):

    #这里不能写成 f=open("data.txt",'a+'）否则会乱码，设置沉utf-8的格式，与getHtml(url):中的encoding一致
    f=open("data.txt",'a+',encoding='utf-8')

    for c in content:
        f.write('标题： {} \t 链接：{} \t 发帖人：{} \t 发帖时间：{} \t 回复数量： {} \n'.format(
            c['title'], c['link'], c['author'], c['creatTime'], c['responseNum']))



url="http://tieba.baidu.com/f?ie=utf-8&kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&red_tag=z0177533255"
page=2


def main(url,page):

    url_list=[]
    #将所需要爬去的url放到列表中
    for i in range(0,page):
        url_list.append(url+'&pn='+str(i*50))

    for u in url_list:
        content=get_content(u)
        writeTxt(content)

if __name__=="__main__":
    main(url,page)
    get_content("http://tieba.baidu.com/f?ie=utf-8&kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&red_tag=z0177533255")




