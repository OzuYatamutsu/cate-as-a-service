from text import cateify
from flask import Flask, request, redirect
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

if __name__ == '__main__':
    if len(argv) == 2:
        app.run(port=argv[1])
    else:
        app.run()

