import os

import requests
import requests

from flask import Flask, render_template, jsonify,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/menu")
def get_menu() :
    return jsonify({"menu" : "팥 붕어빵, 슈크림 붕어빵, 고구마 붕어빵, 치즈 붕어빵, 피자 호빵"})

@app.route("/sales")
def get_sales() :
    return jsonify({"sales" : "200000원"})

@app.route("/coupon")
def get_coupon() :
    return jsonify({"coupon" : "붕어빵 1개 무료 쿠폰!, 10% 할인 쿠폰"})


@app.route("/order",methods = ["POST"])
def get_order() :
    data = request.get_json()
    print(data)
    name = data.get("name")
    coupon = data.get("coupon")
    type_b = data.get("type")
    type_name = data.get("type_name")

    amount = int(data.get("amount"))
    coupon = int(coupon)
    price = int(type_b)
    price = (1 - coupon/100) * price * amount

    return jsonify({"msg" : f"{name} 손님, {type_name} {amount}개 주문이 완료되었습니다. 금액은 {price}원입니다."})

if __name__ == '__main__':
# debug=True 모드는 개발 중에만 사용해야 합니다.
    port = int(os.environ.get("PORT", 5002))  #Render가 주는 PORT 사용
    app.run(host="0.0.0.0", debug=False, port=port)