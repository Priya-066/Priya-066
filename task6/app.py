from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def home():
    name = "Priya"
    return render_template('index.html', name = name)

@app.route('/fruits')
def fruits():
    fruit = ['apple', 'orange', 'banana']
    return render_template('fruits.html', fruits=fruit)

@app.route('/age')
def age():
    age = 20
    return render_template('age.html', age = age)

if __name__ == "__main__":
    app.run(debug=True)