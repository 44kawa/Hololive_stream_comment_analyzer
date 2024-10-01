# Hololive stream comment analyzer

## 環境構築

環境

- OS : Windows 11
- WSL2 : Ubuntu-24.04

### 仮想環境の構築

仮想環境のフォルダを作成する。

```
$ mkdir ~/.venvs
```

次に venv を実行し、仮想環境を構築する。

```
$ python3 -m venv ~/.venvs/hololive_stream_comment_analyzer
```

以下のコマンドを実行し、仮想環境をアクティベイトする。なお、このコマンドはシェルを起動するたびに実行する。

```
source ~/.venvs/hololive_stream_comment_analyzer/bin/activate
```

仮想環境の終了は以下のコマンド。

```
(hololive_stream_comment_analyzer) $ deactivate
```

### Google の環境構築

WSL2 に Google Chrome と chromedirver をインストールする。
Google Chrome のインストール

```
$ sudo apt install google-chrome-stable
```

Chrome が正確に立ち上がることを確認する

```
$ google-chrome
```

GUI の Google Chrome が表示されれば OK。
次に、chrome のバージョンを確認する。

```
$ google-chrome --version
```

対応するバージョンを以下から選択する。
https://googlechromelabs.github.io/chrome-for-testing/

該当するバージョンの zip をダウンロードし、解答。その後/usr/bin ディレクトリに chromedriver を配置する。

```
$ cd /tmp
$ wget https://storage.googleapis.com/chrome-for-testing-public/129.0.6668.70/linux64/chromedriver-linux64.zip
$ unzip chromedriver-linux64.zip
$ sudo cp chromedriver-linux64/chromedriver /usr/bin/
```

chrome と同じバージョンならば OK。

```
$ chromedriver --version
```
