from flask import Flask, jsonify
import subprocess
import json
import datetime

app = Flask(__name__)

@app.route('/amazonapi/<string:qry>')
#Example: http://127.0.0.1:5000/amazonapi/laptops, http://127.0.0.1:5000/amazonapi/earphones
def amazonapi(qry):
    spiderName = 'amazon'
    File = datetime.datetime.now()
    subprocess.check_output(['scrapy','crawl',spiderName,'-a','query='+qry,'-o',File.strftime('Outputs/{}-%d%m%Y-%H%M%S%f').format(qry)+'.json'])
    with open(File.strftime('Outputs/{}-%d%m%Y-%H%M%S%f').format(qry)+'.json') as outfile:
        data = json.loads(outfile.read())
        return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)