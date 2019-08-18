from flask import Flask, render_template
import glob
from datetime import datetime
import os

app = Flask('arthur')

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


app.run(debug=True, host='0.0.0.0', port='3456')