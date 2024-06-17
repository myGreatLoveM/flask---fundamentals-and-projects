from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/')
def home():
    resp = make_response('Welcome to Flask')
    return resp

@app.route('/set_cookie')
def set_cookie():
    resp = make_response('<h1>Set Cookie</h1>')
    resp.set_cookie('foo', 'bar')
    return resp

@app.route('/get_cookie')
def get_cookie():
    print(request.cookies)
    return 'kvnzldvk'

if __name__ == '__main__':
    app.run(debug=True)