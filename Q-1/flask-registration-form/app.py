from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    return f"Thanks {name}, you have registered with email {email}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
