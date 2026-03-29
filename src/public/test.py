from flask import Flask

app = Flask(__name__)

from flask import Response

@app.route('/v1')
def create_account():
    accountpage = open("wisp.js", "r").read()
    return Response(accountpage, mimetype="application/javascript")

if __name__ == '__main__':
    app.run(port=5001) 
