from flask import Flask, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def predict():
    params = pd.DataFrame([request.args.to_dict()])
    return params.to_html()

if __name__ == '__main__':
    app.run(debug=True)
