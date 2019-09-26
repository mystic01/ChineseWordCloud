# Chinese Word Cloud

## 成果範例

![Sample](https://github.com/mystic01/ChineseWordCloud/blob/master/dist/Avengers.png)

## 懶人使用說明
1. 下載[壓縮檔](https://github.com/mystic01/ChineseWordCloud/raw/master/dist/create_word_cloud.zip)並解壓會看到以下目錄結構
```
|- data
|- fonts
|- source
create_word_cloud.exe
```
2. 先點擊 `create_word_cloud.exe` 試試功能環境是否正常，約莫 20 秒黑框視窗關閉，出現 `Avengers.png` 及 `cloud.png` 表示環境 ok！
（如果沒有出現，可以洗洗睡了～XD）

3. 開始使用
- `source` 裡頭可以放置要分析的資料，目前僅支援 `*.xlsx`, `*.docx`, `*.txt`
- `data -> template` 裡頭可以放置要成型的樣板，目前資源 `*.png` 及 `*.jpg`，注意圖片解析度要夠大
- `data -> stopwords.txt` 可以編輯想要去掉的詞彙
- `data -> userdict.txt` 可以編輯想要補充的詞彙
* `stopwords.txt` 與 `userdict.txt` 並不會互斥，例如在 `stopwords.txt` 加入「塔克」，`userdict.txt` 裡頭的「史塔克」一樣會出現在結果圖片上
