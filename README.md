****************************************************************
2021/5/18

jupyter版（google Colaboratory対応）を加えました。　sample.ipynb
****************************************************************






# mooc1
プログラム getDataFromGMap.py　

彦根城の入場者数を取得

jupyter notebook　にそのまま貼り付けるなどして実行

コードの説明

・ライブラリの読み込み

 import populartimes


#populartimesのインストール

 pip install  populartimes-2.0-py3-none-any.whl


・グーグルマップの利用キーの設定　

gid="利用id" 

#利用idは各自で以下のアドレスから取得すること

https://developers.google.com/maps/documentation/javascript/get-api-key?hl=ja


キー例（一時的利用可）

gid="AIzaSyBQv0IZlVassvx8X6_n9ZCUY-nrxWK2w1E" 



・彦根城のプレイス IDの設定　

pid="ChIJw9u_XSsrAmARMIwpeAshKu4" 


#別の場所を指定する場合は、以下のページなどから場所のidを取得してください

https://developers.google.com/maps/documentation/javascript/examples/places-placeid-finder


・データの取得

data=populartimes.get_id(gid, pid)

データは辞書型なので以下のようにアクセス

d1=data['populartimes']

後はデータを利用する

参照
・populartimes詳細

https://github.com/m-wrzr/populartimes (edited)


