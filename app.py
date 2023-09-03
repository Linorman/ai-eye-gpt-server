from flask import Flask, request
from work import Work

app = Flask(__name__)
work = Work()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# 根据form表单的text数据进行预测
@app.route('/api/v1/predict', methods=['POST'])
def predict():
    # 获取输入的文本
    text = request.form['text']
    # 预测
    result = work.predict(text)
    # 返回结果
    return result


if __name__ == '__main__':
    app.run()
