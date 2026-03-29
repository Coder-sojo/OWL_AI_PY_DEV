from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    user_input = request.form['user_input']
    response = f"Owl AI says: You entered '{user_input}'"
    return render_template('result.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)