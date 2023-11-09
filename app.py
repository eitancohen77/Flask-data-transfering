from flask import Flask, render_template, request
import langchain_helper as lch
from dotenv import load_dotenv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# This is the route in which it process the data.
# How this is works is it takes in the user input throught the 
# index.html under templates folder. Then once the user clicks
# submit, the data is stored under user_input variable.
@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']
    print(f"THE INPUT: {user_input}")

    # Once that is done, we call on the lch generate_output function in the
    # langchain_helper.py file. This takes in input gives it to some AI model
    # and we get output from the model.
    output = lch.generate_output(user_input)['output']

    # Now we can return the output as so. 
    # Whatever you name the variable here will be what is used in the final 
    # (results.html) page.
    return render_template('results.html', data=output)

if __name__ == "__main__":
    app.run(debug=True)
