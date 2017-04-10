from text import cateify
from flask import Flask, abort, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    input_text = ''  # TODO
    return cateify(input_text)

app.run()

