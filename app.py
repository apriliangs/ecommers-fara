from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home.html')
def home():
    return render_template('home.html')

@app.route('/checkout.html')
def checkout():
    return render_template('checkout.html')


if __name__ == '__main__':
    app.run(debug=True)
