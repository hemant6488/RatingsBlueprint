# app.py - a minimal flask api using flask_restful
from flask import Flask, render_template
from flask_restful import Api
from api.v1.urls import api_v1 as api_blueprint

app = Flask(__name__)
api = Api(app)

app.register_blueprint(api_blueprint, url_prefix='/api/v1')


@app.route('/')
def get():
    return render_template('template.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
