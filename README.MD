# iqiyi danmu

爱奇艺弹幕 解压 下载

请求类似 `https://cmts.iqiyi.com/bullet/67/00/12345653655432_60_1_8cca2bc9.br`

F12 断点在 `getBarrageBrData`, `console` 执行 main.js 的代码，即可得到一些链接，需要自行排除不存在的链接

将准备好的 br 文件放到一个文件夹下，如：`danmu/`

## 使用

```sh
wget https://github.com/adobe-fonts/source-han-mono/releases/download/1.002/SourceHanMono.ttc
python3 -m venv ./venv
./venv/bin/python3 isntall -r requirements.txt
./venv/bin/python3 main.py -i danmu/ -o 1.jpg
```
