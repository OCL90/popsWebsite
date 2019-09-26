from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/culture')
def culture():
  return render_template('culture.html')

@app.route('/solutions')
def solutions():
  return render_template('solutions.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

if __name__ == '__main__':
  app.run(debug=True)

