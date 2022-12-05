# Author: Olin Gallet
# Date: 4 Dec 2022

from flask import Flask
from airtable import Airtable
import cohere 
import os

app = Flask(__name__)

@app.route('/success/')
def display_success():
    return '200 - Process Success'

@app.route('/failure/')
def display_failure():
    return '401 - Error'

@app.route('/process/',methods = ['POST'])
def process():
    print(request.json)
    return redirect(url_for('success'))

@app.route('/')
def demo():
    co = cohere.Client('') 
    response = co.generate( 
    model='xlarge', 
    prompt='Product: Drill Taps\nKeywords: drill, carbide tip\nExciting Product Description:', 
    max_tokens=50, 
    temperature=0.8, 
    k=0, 
    p=1, 
    frequency_penalty=0, 
    presence_penalty=0, 
    stop_sequences=["--"], 
    return_likelihoods='NONE') 
    base_key = os.environ['AIRTABLE_BASE_KEY']
    table_name = 'Estate'
    api_key = os.environ['AIRTABLE_API_KEY']
    airtable = Airtable(base_key, table_name, api_key)
    data = {'product_sku':{'text': '000'}, 'product_name' : 'Drill Taps', 'product_description' : response.generations[0].text, 'product_image' : {'url':'http://www.olingallet.com'}}
    airtable.insert(data)
    return 'Done' 

if __name__ == '__main__':
    app.run()