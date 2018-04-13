import requests
import json,re

pagenum =1
while True:
    url='http://pc.k.360kan.com/pc/list?n=20&p='+str(pagenum)+'&f=json&ajax=1&uid=30af28d856b010645e71555d04ef7124&channel_id=2&dl='
    r = requests.get(url)
    page = json.loads(r.text)
    data = page['data']['res']
    for res in data:
        title = res['t']
        if title.endswith('?'):
            title.replace('?','!')
        print(title)
        data_id = re.findall('detail/(.*?)\?', res['videoUrl'])[0]
        play_url = 'http://pc.k.360kan.com/pc/play?id='+data_id
        rv = requests.get(play_url)
        rvpage = json.loads(rv.text)
        vedio_url = rvpage['data']['url']
        vedio_re= requests.get(vedio_url)
        with open("F:\python_workplace\download\FastVedio\\"+title+'.mp4','wb') as f:
            f.write(vedio_re.content)
        if len(data) == 20:
            pagenum+=1
        else:
            break


