import requests
import json,re

pagenum =1
while True:
    ##  参数 n 为每页显示的数量  p 为页数  channel_id为频道
    url='http://pc.k.360kan.com/pc/list?n=10&p='+str(pagenum)+'&f=json&ajax=1&uid=30af28d856b010645e71555d04ef7124&channel_id=2&dl='
    #通过初始地址获取json格式的data数据
    r = requests.get(url)
    page = json.loads(r.text)
    data = page['data']['res']
    #遍历data获取视频名称与播放地址（下载地址）
    for res in data:
        title = res['t']
        if title.endswith('?'):
            title.replace('?','!')
        print(title)
        data_id = re.findall('detail/(.*?)\?', res['videoUrl'])[0]
        play_url = 'http://pc.k.360kan.com/pc/play?id='+data_id
        #通过播放地址可获取一个视频的播放接口形式的json数据，数据中包含了视频下载地址
        #通过获取下载地址，获取地址内容，进行下载
        rv = requests.get(play_url)
        rvpage = json.loads(rv.text)
        vedio_url = rvpage['data']['url']
        vedio_re= requests.get(vedio_url)
        with open("F:\python_workplace\download\FastVedio\\"+title+'.mp4','wb') as f:
            f.write(vedio_re.content)
       #每一页视频数量为10，当数量不为10的时候，说明已到最后一页，则不在进行页数叠加 
        if len(data) == 10:
            pagenum+=1
        else:
            break


