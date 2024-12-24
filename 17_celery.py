#分布式pip install celery(分布式管道，分发任务) redis(内存型数据库) eventlet(异步线程)
#backed，处理完任务数据存在哪里，0号数据库，broker分发器分发任务
from celery import Celery
import requests
from bs4 import BeautifulSoup

app = Celery('tasks',
             broker='redis://127.0.0.1:6379/1',
             backend='redis://127.0.0.1:6379/0')

@app.task#表明式celery任务
def get_html():
    html = requests.get('https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4')
    soup = BeautifulSoup(html.text, 'lxml')
    links = soup.select('h2 a')
    result = []
    for link in links:
        link = link['href']
        result.append(link)
    return '|'.join(result)
#运行：celery -A 17_celery worker -l info -P eventlet