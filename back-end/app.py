from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/about')
def about():
    return 'About Page'

@app.route('/contact')
def contact():
    return 'Contact Page'

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form['data']
    return f'Data received: {data}'

@app.route('/api/data')
def api_data():
    data = {'key': 'value'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
