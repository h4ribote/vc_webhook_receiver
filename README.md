# vc_webhook_receiver
fastapiを用いてVirtualCryptoのwebhookを受け取る例みたいなやつ  
私のような初心者にとってはvcのドキュメントに書いてある内容だけだと~~ちょっと分かりづｒ~~色々調べないとすぐに稼働できなくて辛かったので

# 使い方
0. Pythonをダウンロード・インストール(https://www.python.org/downloads/)
1. VirtualCryptoで色々操作
   1. 新規アプリケーションの作成
   2. 公開鍵のコピー
3. requirements.txt
   ```
   pip install -r requirements.txt
   ```
4. config.pyの設定
   ```python
   PUBLIC_KEY:str = "コピーした公開鍵を貼り付け"
   ```
5. RUN!!
   ```
   python3 main.py
   ```
6. VirtualCryptoでWebhookの"webhookを受け取るurl"を指定して保存(設定が正常に保存されていることを確認すること)
7. 好みの処理(やりたかったあんなことやこんなこと！)を追記していく
