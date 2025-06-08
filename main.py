from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('intro.html') 

@app.route('/intro')
def intro():
    return render_template('intro.html') 

@app.route('/methods')
def methods():
    return render_template('methods.html') 

@app.route('/concludion')
def concludion():
    return render_template('concludion.html') 

if __name__ == '__main__':
    app.run(debug=True)