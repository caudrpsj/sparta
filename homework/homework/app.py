from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


## API 역할을 하는 부분
@app.route('/shoppings', methods=['POST'])
def write_shoppigs():
    name_receive = request.form['name_give']
    number_receive = request.form['number_give']
    address_receive = request.form['address_give']
    zip_receive = request.form['zip_give']


    shopping = {
       'name': name_receive,
       'number': number_receive,
       'address': address_receive,
       'zip': zip_receive
    }

    db.shopping.insert_one(shopping)
    return jsonify({'result': 'success', 'msg': '구매가 성공적으로 실행되었습니다.'})


@app.route('/shoppings', methods=['GET'])
def read_shoppings():
    shoppings = list(db.shopping.find({},{'_id':0}))
    return jsonify({'result': 'success', 'shoppings': shoppings})


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)