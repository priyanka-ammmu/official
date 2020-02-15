import flask
import json
import requests

app = Flask(__name__)

@app.route('/notification/SaveMessage', methods=['POST'])
def savemessage():
    Url = ''
    data = {"Topic": "Hot News","Message":"A Mobie Shoot Happening in Madurai"}
    r = requests.post(url=Url,json=data)
    print(r.status_code)
    if r.status_code == 200:
      obj = {"status":200,"Reply":"Message Send to Topic"}
    return jsonify (obj)
    
@app.route('/notification/GetMessage?Topic=Hot-News', methods=['GET'])
def getmessage():
    Url = 'https://aws.amazon.com/getting-started/projects/buid-serverless/projects/buid-serverless-web-app-lambda-apigateway-s3-dynamodb-cognito/'
    r = requests.get(url=Url)
    d = r.json()
    if r.status_code == 200:
      obj = {"status":200,"Messages":d}
    return jsonify (obj)

@app.route('/', methods=['GET'])
def hello():
    return 'helloworld!'
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port='3000')
