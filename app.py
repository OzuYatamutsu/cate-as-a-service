#!/usr/bin/env python3

from text import cateify
from flask import Flask, abort, request, redirect
from sys import argv

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index_post():
    input_text = request.form['text']
    return cateify(input_text)

@app.route('/', methods=['GET'])
def index_get():
    # (Redirects to repo)
    redirect_location = 'https://github.com/OzuYatamutsu/cateify-as-a-service'
    return redirect(redirect_location)

@app.route('/cate', methods=['GET'])
def cate_get():
    input_text = request.args.get('text')
    if input_text:
        return cateify(input_text)
    else:
        abort(400)

if __name__ == '__main__':
    if len(argv) == 2:
        app.run(port=argv[1])
    else:
        app.run()

