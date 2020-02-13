from flask import Flask
from flask import render_template
import pymysql
import quickstart

con = pymysql.connect('localhost', 'valentin', 'root', 'test_db', 3306)
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM user")
    result = cur.fetchone()
    print("Data: {}".format(result))

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

