# 出席管理システム

# 用途・目的
これらのファイルは出席管理システムに関するプログラムである．

app.pyはFlaskアプリケーションとHTMLによるWebサイトのプログラムである．

Webサイトにて名前を入力して出席をすることで記録をとることが目的である．

出席の時間や名前はログをcsvファイルに保存する．利用者はPCやスマートフォンでWebサイトにアクセスして出席する．

# プログラム紹介
## app.py
Webサイトを運用し，ログファイルを生成するプログラムである．

# 使用言語
使用言語はPythonでバージョンは3.12.3である．

# 必要なパッケージ
Flaskが必要

venvによる仮想環境を構築してからpip install flaskを実行してインストール可能

venvの仮想環境構築方法はこちらを参照：https://qiita.com/fiftystorm36/items/b2fd47cf32c7694adc2e

# 実行方法

Ubuntu等でvenvによる仮想環境を構築し，app.pyを下記の方法で実行する．
~~~
python3 app.py
~~~

その後，実行結果の画像の通りになっていればFlaskによるWebサイトが実行できている．
Webサイトには，http://127.0.0.1:5000でアクセス可能

# 実行結果
app.pyの実行結果
<img width="939" height="251" alt="image" src="https://github.com/user-attachments/assets/2c168b37-85a2-465e-a226-cd55e6f29293" />

Webページの表示
<img width="902" height="548" alt="image" src="https://github.com/user-attachments/assets/64f512c2-6ad8-4e92-937e-684efd3c39ba" />

# おわりに
app.pyの実行後に保存されたcsvファイルは以下のようになっている．

attendance_20251102.csvの内容
<img width="886" height="52" alt="image" src="https://github.com/user-attachments/assets/761c0d96-622e-4e46-9677-8a6e84da46a1" />


