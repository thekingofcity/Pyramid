from Pyramid import Pyramid
from multiprocessing import Process, Queue, freeze_support
#import json, time
from flask import Flask, render_template, request, jsonify
APP = Flask(__name__, static_url_path='')
# APP = Flask(__name__)
INQ = Queue()
OUTQ = Queue()
ARGS = {"isTTS": False, "buy": 0, "sell": 0}
INQ.put(ARGS)


@APP.route('/query', methods=['GET'])
def query():
    if OUTQ.empty():
        raise Exception("OUTQ.empty()")
    while not OUTQ.empty():
        tmpOUT = OUTQ.get()
    OUTQ.put(tmpOUT)
    buyhigh = request.args.get('buyhigh', -2)
    buylow = request.args.get('buylow', -2)
    sellhigh = request.args.get('sellhigh', -2)
    selllow = request.args.get('selllow', -2)
    # print(ARGS)
    # print(tmpOUT)
    return jsonify(sell=tmpOUT["sell"], buy=tmpOUT["buy"])
    # if request.method == 'POST':
    #     pass
    # else:
    #     pass
    # name = request.form['buyhigh']
    # email = request.form['buylow']
    # return render_template('index.html', name=tmp["sell"], email=tmp["buy"])
    

@APP.route('/isTTS', methods=['GET'])
def isTTS():
    ARGS["isTTS"] = request.args.get('isTTS', False)
    ARGS["isTTS"] = True
    while not INQ.empty():
        tmpIN = INQ.get()
    INQ.put(ARGS)
    return jsonify(result="OK")


@APP.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    PYR = Pyramid(INQ, OUTQ)
    PYR.start()
    # print("本地时间为 :", time.asctime(time.localtime(time.time())))
    APP.run(host='0.0.0.0')
    