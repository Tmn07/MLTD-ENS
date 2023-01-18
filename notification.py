# coding: UTF-8

from datetime import datetime
import pytz
import requests

currentDateAndTime_jp = datetime.now(tz=pytz.timezone('Asia/Tokyo'))  # for Japan time zone

currentTime = currentDateAndTime_jp.strftime("%Y-%m-%dT%H:%M:%S")
print("The current time is", currentTime)
currentDate = currentDateAndTime_jp.strftime("%Y-%m-%d")

# currentTime = "2020-08-10T20:59:59"
url = "https://api.matsurihi.me/mltd/v1/events?at="
# 2020-08-03T15:01:00

r = requests.get(url+currentTime)
now_event = r.json()

if len(now_event) == 0:
    print('no event now.')
else:
    event_name = now_event[0]['name']
    endDate = now_event[0]['schedule']['endDate'][:10]
    if currentDate == endDate:
        print(f'{event_name} final day!')
        # sendmail()
        pass
    else:
        print(f'{event_name} 进行中.')

import siblib

email = "519043202@qq.com"
nickename = "Tmn07"
subject = "麻辣土豆活动结束通知"
content = f"<p>{event_name} 活动还有半小时要结束拉，记得清体力完成任务~</p>"

content += "<p>如果不想再订阅此活动结束提醒服务，请点击 <a href='http://tmn07.com/app'>此链接</a></p>" \
            "<p>未来想要再次订阅此服务请访问 <a href='http://tmn07.com/mltd/notice'>tmn07.com/mltd/notice</a></p>"

siblib.sendMail(email, nickename, subject, content)
