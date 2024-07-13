from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


students = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_student', methods=['POST'])
def add_student():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    roll_number = request.form['roll_number']
    cgpa = request.form['cgpa']
    courses = request.form.getlist('courses')
    
    student = {
        'first_name': first_name,
        'last_name': last_name,
        'roll_number': roll_number,
        'cgpa': cgpa,
        'courses': courses
    }
    students.append(student)
    
    return redirect(url_for('index'))

@app.route('/search_student', methods=['POST'])
def search_student():
    query = request.form['search_query']
    results = []

    for student in students:
        if query in student['first_name'] or query in student['last_name'] or query == student['roll_number']:
            results.append(student)

    return render_template('index.html', results=results)

@app.route('/search_course', methods=['POST'])
def search_course():
    course_id = request.form['course_id']
    results = []

    for student in students:
        if course_id in student['courses']:
            results.append(student)

    return render_template('index.html', results=results)

@app.route('/delete_student/<roll_number>', methods=['GET'])
def delete_student(roll_number):
    for student in students:
        if student['roll_number'] == roll_number:
            students.remove(student)
            break
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
