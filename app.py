from flask import Flask,redirect
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('baidu.html')
#    return 'Hello World!'

@app.route('/user/<username>')
def baidu_page(username):
    productname = '钳工工具'
    productprice = '10.00'
#    return render_template('baidu.html',name=username,var1=productname,var2=productprice)
    return render_template('baidu.html',**locals())

@app.route('/baidu')
def baidu():
   return render_template('google.html')

if __name__ == '__main__':
    app.run()
