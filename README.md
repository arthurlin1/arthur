# arthur

## 專案
我練習用網站

## 成品展示
[我的作品](https://arthursap.herokuapp.com/)
![](https://github.com/grand-coder/pythondiary/raw/master/index.png)

## 使用技術
--------- | ---------
PYTHON 3 | 程式編寫
flask in python | 需要import的東西 
HTML/CSS | 網頁表示和排版
Heroku   | 託管網頁
Github   | 存放原始碼

## 程式碼片段
ˋˋˋ python
@app.route('/category/<c>')
def category(c):
  fs = glob.glob("articles/" + c + "/*.txt")
  fill = []
  
  for b, f in enumerate(fs):
    y = open(f)
    some = y.read()
    y.close()
    fp = f.split('/')[-1].replace('.txt', '')
    utc = datetime.utcfromtimestamp(os.path.getmtime(f))
    
    t = (b, fp, str(utc), some)
    fill.append(t)
  return render_template("category.html", cat=fill, title=c)

@app.route('/')
def home():
  temp = glob.glob("articles/*")
  fill = []
  for i in temp:
    length = len(glob.glob(i+"/*.txt"))
    cate =i.replace("articles/", "")
    f = (cate, length)
    fill.append(f)
  return render_template("index.html", cat=fill)
ˋˋˋ
