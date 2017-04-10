from text import cateify
from flask import Flask, request, redirect
 
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

app.run()

