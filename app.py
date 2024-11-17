from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Auto-incrementing ID
    question = db.Column(db.Text, nullable=False)  # The question text
    answer = db.Column(db.Text, nullable=False)  # The answer text
    explanation = db.Column(db.Text, nullable=True)  # Explanation (optional)
    question_type = db.Column(db.String(50), nullable=False)  # Type of question

    def __repr__(self):
        return f'<Question {self.question}>'

@app.route('/quiz')
def quiz():
    with app.app_context():
        questions = Question.query.all()
        # Pass questions to the HTML template
        return render_template('quiz.html', questions=[
            {
                'id': q.id,
                'question': q.question,
                'answer': q.answer,
                'options': [q.answer, "Option 1", "Option 2", "Option 3"],  # Add fake options
                'explanation': q.explanation,
                'type': q.question_type
            }
            for q in questions
        ])

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    with app.app_context():  # Ensure proper application context
        db.create_all()  # This will create the app.dbb file and the tables
        print("Database initialized!")

    app.run(debug=True)