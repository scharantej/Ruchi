
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/lesson1')
def lesson1():
    return render_template('lesson1.html')

@app.route('/exercise1')
def exercise1():
    return render_template('exercise1.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get user input from the form
        answer = request.form.get('answer')

        # Check if the answer is correct
        if answer == 'correct_answer':
            # Provide positive feedback
            return render_template('correct.html')
        else:
            # Provide negative feedback
            return render_template('incorrect.html')

@app.route('/progress')
def progress():
    # Get user's progress from the database
    progress = get_progress()

    return render_template('progress.html', progress=progress)

if __name__ == '__main__':
    app.run(debug=True)
