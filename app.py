from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask! Welcome to your first app."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/insights')
def insights():
    return render_template('insights.html')

@app.route('/model')
def model():
    return render_template('model.html')

if __name__ == '__main__':
    app.run(debug=True)

