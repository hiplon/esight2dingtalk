from flask import Flask, request, json
import requests

def senddatatodingtalk(alert_message):
    postdata=alert_message
    url='https://oapi.dingtalk.com/robot/send?access_token=DINGTALK_ROBOT_TOKEN'
    message_send={
	"msgtype": "text",
	"text": {"content": postdata},
	}
    headers={'Content-Type': 'application/json'}
    fb=requests.post(url,data=json.dumps(message_send),headers=headers)
    return fb

app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'smsrevice'
 
@app.route('/smstodingtalk', methods=['GET','POST'])
def smstodingtalk():
    username = request.args.get('username')
    if username == 'artisan':
    	message = request.args.get('content')
    	print senddatatodingtalk(message)
    	return 'Success'
    else:
	return 'Error'
 
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=0)

