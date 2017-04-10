from text import cateify
from flask import Flask, request, redirect
from sys import argv
from json import loads
 
app = Flask(__name__)

@app.route('/', methods=['POST'])
def index_post():
    input_text = ''
    
    try:
        input_text = request.get_json(force=True)
        input_text = input_text.get('text', '')
    except Exception as e:
        if request.form is not None:
            input_text = request.form.get('text', '')
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

