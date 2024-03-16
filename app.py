import os
from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    
#app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 80)))
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)