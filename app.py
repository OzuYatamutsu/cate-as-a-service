from text import cateify
from flask import Flask, request
 
app = Flask(__name__)

@app.route('/', methods=['POST'])
def index_post():
    if request.method == 'GET':
        return ''
    input_text = request.form['text']
    return cateify(input_text)

@app.route('/', methods=['GET'])
def index_get():
    return ''

app.run()

