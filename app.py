from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False)
    explanation = db.Column(db.String, nullable=True)
    question_type = db.Column(db.String, nullable=False)
    options = db.Column(db.String, nullable=True)  # Add this line

    def __repr__(self):
        return f'<Question {self.question}>'

@app.route('/quiz/')
def history_quiz():
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
def homepage():
    return render_template('homepage.html')

@app.route('/enroll')
def enroll():
    return render_template('enroll.html')


def generate_options(question):
    """
    Generate options dynamically based on the question context.
    :param question: The Question object.
    :return: List of options.
    """
    if question.question_type == "Geography":
        return [question.answer, "London", "Tokyo", "New York"]
    elif question.question_type == "Math":
        return [question.answer, "10", "20", "30"]
    elif question.question_type == "Literature":
        return [question.answer, "J.K. Rowling", "George Orwell", "Jane Austen"]
    else:
        # Default options for unknown types
        return [question.answer, "Option 1", "Option 2", "Option 3"]



@app.route('/quiz/<grade>/<book>')
def quiz_page(grade, book):
    with app.app_context():
        questions = Question.query.all()
        question_data = []

        for q in questions:
            # Generate options based on question context
            options = generate_options(q)  # Dynamic option generation function

            question_data.append({
                'id': q.id,
                'question': q.question,
                'answer': q.answer,
                'options': options,
                'explanation': q.explanation,
                'type': q.question_type
            })

        # Pass questions to the template
        return render_template('quiz.html', grade=grade, book=book, questions=question_data)


if __name__ == '__main__':
    with app.app_context():  # Ensure proper application context
        db.create_all()  # This will create the app.dbb file and the tables
        print("Database initialized!")

    app.run(debug=True)