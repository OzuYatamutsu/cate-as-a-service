#!/usr/bin/env python3

from text import cateify
from flask import Flask, abort, request, redirect, Response
from sys import argv
from json import loads

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index_post():
    input_text = ''

    try:
        input_text = request.get_json(force=True)
        input_text = input_text['text']
    except Exception as e:
        if request.form is not None and 'text' in request.form:
            input_text = request.form['text']
        else:
            abort(400)
    return __generate_meme_response(cateify(input_text))

@app.route('/', methods=['GET'])
def index_get():
    # (Redirects to repo)
    redirect_location = 'https://github.com/OzuYatamutsu/cate-as-a-service'
    return redirect(redirect_location)

@app.route('/cate', methods=['GET'])
def cate_get():
    input_text = request.args.get('text')
    if input_text:
        return __generate_meme_response(cateify(input_text))
    else:
        return abort(400)

@app.route('/cate/<string:text>', methods=['GET'])
def cate_get_extended_route(text):
    return __generate_meme_response(cateify(text))

def __generate_meme_response(text: str) -> Response:
    response = Response(text)
    
    # Add headers
    response.headers['Meme-Type'] = 'text/c a t e'

    return response

if __name__ == '__main__':
    if len(argv) == 2:
        app.run(port=argv[1])
    else:
        app.run()

