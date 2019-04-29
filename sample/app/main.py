from flask import Flask
from flask import request

from servingHandler import makeRequest, updateConfigurations, getConfigurations

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/testPredictions')
def singleRequest():
    return makeRequest()

@app.route('/reloadConfigurations')
def reload():
    return str(updateConfigurations())

@app.route('/getConfigurations')
def getConf():
    f = open("models.conf", "r")
    data = f.read()
    f.close()
    return data

@app.route('/updateConfigurations', methods = ['POST'])
def updateConf():
    data = request.data
    f = open("models.conf", "w")
    f.write(data)
    f.close()
    return str(updateConfigurations())

if __name__ == '__main__':
    app.run()