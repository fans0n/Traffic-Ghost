import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def showData():
    os.system(python )
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
