该项目提供了web服务调用dubbo接口的测试方案,支持集成到postman等各种测试框架!

## 使用示例

假如你的web服务器主机与端口是127.0.0.1:9090,那么,通过调用如下链接可以调用dubbo接口获取结果:

http://127.0.0.1:9090/dubbo?host=10.37.46.152&port=20880&method=queryCpsConfig&args={"sellerId":"1808844800"}

参数的含义是:

* host 接口所在的dubbo服务地址
* port 接口所在的dubbo服务端口
* method 要执行的方法/测试的接口
* args 方法的参数

返回结果如下:

```json
{"code":0,"msg":"success","result":{"code":0,"message":null,"module":{"cpsFeeRatio":10,"shopConfigModify":false},"success":true}}
```

响应的含义是:

* code 为0时表示dubbo接口调用正常
* msg 如果调用失败,会返回相应的异常信息
* result dubbo接口的返回结果


## 部署说明

在要部署的服务器(linux)上,执行:

```bash
# 在开发环境执行
pyinstaller --hidden-import flask --hidden-import flask_cors -F server.py
# 在生产环境执行
git clone https://gitlab.vdian.net/base-qa/dubbo-api-test-python.git
cd dubbo-api-test-python
nohup ./dist/server &
```

然后访问你服务器的9090端口即可查看站点内容