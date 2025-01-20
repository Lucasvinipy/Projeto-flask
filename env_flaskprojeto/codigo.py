from flask import Flask , render_template

app = Flask(__name__)

@app .route('/')
def ola_mundo():
    return render_template('index.html')

@app .route('/sobre')
def sobre():
    return " loren lore n loren"

app.run(debug=True)