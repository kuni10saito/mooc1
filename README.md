# mooc1
プログラムコード（彦根城の入場者数を取得）

import populartimes

#Google Maps API key 
gid="AIzaSyBQv0IZlVassvx8X6_n9ZCUY-nrxWK2w1E" 
#彦根城のプレイス ID
pid="ChIJw9u_XSsrAmARMIwpeAshKu4" 

data=populartimes.get_id(gid, pid)


参照
・populartimes詳細
https://github.com/m-wrzr/populartimes (edited)

populartimesのインストール
pip install  populartimes-2.0-py3-none-any.whl
whlファイルは上記アドレスで取得

・Google Maps API key取得
https://developers.google.com/maps/documentation/javascript/get-api-key?hl=ja

・地図からplace id を得る方法
https://developers.google.com/places/place-id?hl=ja
