import random
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def output():
    return "로또번호 생성기"

@app.route("/Lotto")
def lotto():
    lotto_list = list(range(1,46))
    lotto_num = sorted(random.sample(lotto_list,6 ))
    return jsonify(lotto_num)
        
if __name__ == "__main__":
    app.run()
