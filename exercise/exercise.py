from flask import Flask


app = Flask(__name__)

@app.route('/api/v2/exercise/<word>')
def dictionary(word):
    return {"definition": word.title(), "word": word}

app.run()