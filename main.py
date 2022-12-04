# Author: Olin Gallet
# Date: 4 Dec 2022

from flask import Flask

app = Flask(__name__)

@app.route('/success/')
def display_success():
    return '200 - Process Success'

@app.route('/failure/')
def display_failure():
    return '401 - Error'

@app.route('/',methods = ['POST'])
def process():
    print(request.args)
    key = request.args.get('')
    print(key)
    return redirect(url_for('success'))

if __name__ == '__main__':
    app.run()