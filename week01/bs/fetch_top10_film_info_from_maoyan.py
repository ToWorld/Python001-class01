import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from fake_useragent import UserAgent

# 设置请求头
# 第一次使用时, user-agent就足够了
# 后续再次请求建议填充cookie，防止过早被禁
# 如何获取对应网站的cookies?
header = {
    "user-agent": UserAgent().random,
    "cookie": "__mta=119806007.1593107842173.1593161979973.1593161980009.10; uuid_n_v=v1; uuid=4CE7F7F0B70D11EA9B3075693A212BAFD840DB84EF7745AE8C6E0232A8675E7C; _csrf=f61d9a8c249a5f79121e023b66d09dbe7b9686863d566aadb34ea3d63665ba07; mojo-uuid=cba42ebfbac7499726e6f55dac5fb937; _lxsdk_cuid=172eca072f0c8-0134bf7889df4-31617402-13c680-172eca072f1c8; _lxsdk=4CE7F7F0B70D11EA9B3075693A212BAFD840DB84EF7745AE8C6E0232A8675E7C; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593171654,1593174010,1593189473,1593228626; mojo-trace-id=4; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593228965; __mta=119806007.1593107842173.1593161980009.1593228965406.11; _lxsdk_s=172f3d3885e-182-eff-2e8%7C%7C5"
}

# 目标网站网址
myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl,headers=header)

bs_info = bs(response.text, 'html.parser')
top10_film_info = []
name = ['name', 'tag', 'time']
counter = 0
for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    all_child_div = tags.find_all('div')
    try:
        file_name = all_child_div[0].text.split('\n')[1].strip(' ')
        file_tag = all_child_div[1].text.split('\n')[2].strip(' ')
        file_time = all_child_div[3].text.split('\n')[2].strip(' ')
        top10_film_info.append([file_name, file_tag, file_time])
    except Exception as e:
        print('ignore %s' % e)
        continue
    counter += 1
    if counter == 10:
        break
pd.DataFrame(columns=name, data=top10_film_info).to_csv('top10_film_info.csv', encoding='utf-8')
