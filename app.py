import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Fuck Egon!!!!!"

if __name__ == "__main__":
    port = int(os.environs.get('PORT', 9001))
    app.run(host='0.0.0.0' , port=port)