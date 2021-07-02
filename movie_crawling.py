import requests
from bs4 import BeautifulSoup
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler

bot = telegram.Bot(token='token') #enter your own token
url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20210623"
def job_function():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    imax = soup.select_one('span.imax')
    if imax:
        imax = imax.find_parent('div', class_='col-times')
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        bot.sendMessage(chat_id="chat_id", text="{}의 IMAX 영화가 상영중입니다.".format(title)) #enter the your own chat_id
        sched.pause()


sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=10)
sched.start()


