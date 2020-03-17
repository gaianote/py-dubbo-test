import sys
import telnetlib
import platform
import json

from flask import Flask, jsonify, request,redirect
from flask_cors import CORS


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/dubbo', methods=['GET'])
def invoke():
    res = {"code":0,"msg":"","result":""}
    host,port,method,args = request.args.get("host"),request.args.get("port"),request.args.get("method"),request.args.get("args")
    if not (host and port and method):
        res["code"] = 3000
        res["msg"] = "参数错误"
        return jsonify(res)
    cmd = "invoke {method}({args})".format(method=method,args=args)
    try:
        tn = telnetlib.Telnet(host,port,timeout = 1)
    except Exception as e:
        res["code"] = 1000
        res["msg"] = "连接到dobbu服务超时,请确认ip与端口号是否正确,以及当前环境是否可以连通"
    else:
        tn.write(cmd.encode("GBK") + b"\n")
        byte_result = tn.read_until(b"dubbo>")
        result = byte_result.decode("GBK").split('elapsed')[0].strip()
        try:
            res["result"] = json.loads(result)
            res["msg"] = "success"
        except Exception as e:
            res["code"] = 2000
            res["msg"] = "duboo接口调用异常"
            res["result"] = str(result)
    return jsonify(res)



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=9090)


