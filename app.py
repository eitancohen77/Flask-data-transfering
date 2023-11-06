from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/petGenerator')
def petGen():
    return render_template('petGen.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']
    print(f"THE INPUT: {user_input}")

    return ""
if __name__ == "__main__":
    app.run(debug=True)
