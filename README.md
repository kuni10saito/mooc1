# mooc1
プログラム（彦根城の入場者数を取得）

import populartimes
gid="AIzaSyBQv0IZlVassvx8X6_n9ZCUY-nrxWK2w1E" #Google Maps API key For Saito
pid="ChIJw9u_XSsrAmARMIwpeAshKu4" #彦根城のプレイス ID


data=populartimes.get_id(gid, pid)
d1=data['populartimes']

import pandas as pd
df = pd.DataFrame()
col_list=[]
for i in range(len(d1)):
   m = d1[i]
   df[i]=m['data']
   col_list.append(m['name'])

df.columns=col_list
df.to_csv('week.csv')


参照
populartimes詳細
https://github.com/m-wrzr/populartimes (edited)

populartimesは
pip install  populartimes-2.0-py3-none-any.whl
でインストール

Google Maps API key取得
https://developers.google.com/maps/documentation/javascript/get-api-key?hl=ja

地図からplace id を得る方法
https://developers.google.com/places/place-id?hl=ja
