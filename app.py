from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
from datetime import datetime
import random

app = Flask(__name__)
# Use environment variable for secret key in production; fallback for local dev
app.secret_key = os.environ.get('SECRET_KEY', 'somerset_college_secret_key_2024')

# Nigerian Educational Scheme Subjects
# Core subjects for all levels
core_subjects = [
    'English Language',
    'Mathematics',
    'Basic Science',
    'Basic Technology',
    'Social Studies',
    'Civic Education',
    'Christian Religious Studies',
    'Islamic Religious Studies',
    'Cultural and Creative Arts',
    'Physical and Health Education',
    'Computer Studies',
    'Agricultural Science',
    'Home Economics',
    'Business Studies',
    'French',
    'Hausa',
    'Yoruba',
    'Igbo'
]

# Senior Secondary subjects (SS1-SS3)
ss_subjects = [
    'English Language',
    'Mathematics',
    'Biology',
    'Chemistry',
    'Physics',
    'Geography',
    'Government',
    'Economics',
    'Literature in English',
    'Computer Science',
    'Civic Education',
    'Agricultural Science',
    'Further Mathematics',
    'History',
    'Commerce',
    'Christian Religious Studies',
    'Islamic Religious Studies',
    'Fine Arts',
    'Physical Education',
    'Music',
    'French',
    'Hausa',
    'Yoruba',
    'Igbo',
    'Food and Nutrition',
    'Technical Drawing',
    'Woodwork',
    'Metalwork',
    'Electronics',
    'Auto Mechanics'
]

# Classes (JSS1–JSS3 and SS1–SS3)
classes = ['JSS1', 'JSS2', 'JSS3', 'SS1', 'SS2', 'SS3']

# Generate Teachers for Nigerian Educational Scheme
teachers = []

# Create teachers for core subjects (JSS)
core_teacher_id = 1
for subject in core_subjects:
    teacher_name = f"Teacher {core_teacher_id:03d}"
    teachers.append({
        'id': core_teacher_id,
        'name': teacher_name,
        'subject': subject,
        'level': 'JSS',
        'email': f"{teacher_name.lower().replace(' ', '')}@someret.edu",
        'username': f"teacher{core_teacher_id:03d}",
        'password': 'teacher123'
    })
    core_teacher_id += 1

# Create teachers for SS subjects
for subject in ss_subjects:
    # Skip if teacher already exists for this subject
    if not any(t['subject'] == subject for t in teachers):
        teacher_name = f"Teacher {core_teacher_id:03d}"
        teachers.append({
            'id': core_teacher_id,
            'name': teacher_name,
            'subject': subject,
            'level': 'SS',
            'email': f"{teacher_name.lower().replace(' ', '')}@someret.edu",
            'username': f"teacher{core_teacher_id:03d}",
            'password': 'teacher123'
        })
        core_teacher_id += 1

# Generate Courses according to Nigerian Educational Scheme
courses = []

# JSS Courses (Core subjects)
jss_course_id = 1
for subject in core_subjects:
    # Find teacher for this subject
    subject_teachers = [t for t in teachers if t['subject'] == subject and t['level'] == 'JSS']
    assigned_teacher = subject_teachers[0] if subject_teachers else teachers[0]
    
    courses.append({
        'id': jss_course_id,
        'name': subject,
        'level': 'JSS',
        'teacher': assigned_teacher['name'],
        'credits': 2,
        'students': random.randint(30, 80)
    })
    jss_course_id += 1

# SS Courses (Senior Secondary subjects)
for subject in ss_subjects:
    # Find teacher for this subject
    subject_teachers = [t for t in teachers if t['subject'] == subject and t['level'] == 'SS']
    assigned_teacher = subject_teachers[0] if subject_teachers else teachers[0]
    
    courses.append({
        'id': jss_course_id,
        'name': subject,
        'level': 'SS',
        'teacher': assigned_teacher['name'],
        'credits': 3,
        'students': random.randint(20, 60)
    })
    jss_course_id += 1

# Generate Students (500 + 70 more = 570)
students = []
for i in range(1, 571):
    student_name = f"Student {i:03d}"
    grade = random.choice(classes)
    
    # Assign appropriate courses based on grade level
    if grade.startswith('JSS'):
        # JSS students take core subjects
        enrolled_courses = random.sample(core_subjects, k=min(8, len(core_subjects)))
    else:
        # SS students take a mix of core and SS subjects
        ss_core = ['English Language', 'Mathematics', 'Biology', 'Chemistry', 'Physics']
        ss_elective = random.sample([s for s in ss_subjects if s not in ss_core], k=3)
        enrolled_courses = ss_core + ss_elective
    
    students.append({
        'id': i,
        'name': student_name,
        'grade': grade,
        'courses': enrolled_courses,
        'username': f"student{i:03d}",
        'password': 'student123',
        'email': f"{student_name.lower().replace(' ', '')}@someret.edu"
    })

# Enforce specific class distribution examples after generation
# Example targets: JSS1 = 50 students, JSS2 = 35 students
desired_class_counts = {
    'JSS1': 50,
    'JSS2': 35,
}

# Build an index list to reassign grades deterministically yet randomly distributed
all_indices = list(range(len(students)))
random.shuffle(all_indices)

start_idx = 0
for cls_name, count in desired_class_counts.items():
    end_idx = start_idx + count
    for idx in all_indices[start_idx:end_idx]:
        students[idx]['grade'] = cls_name
    start_idx = end_idx

# Assign remaining students evenly across other classes
remaining_classes = [c for c in classes if c not in desired_class_counts]
remaining_indices = all_indices[start_idx:]
for index, idx in enumerate(remaining_indices):
    students[idx]['grade'] = remaining_classes[index % len(remaining_classes)]

## Teachers generated above

## Courses generated above

announcements = [
    {'id': 1, 'title': 'Parent-Teacher Conference', 'content': 'Parent-teacher conferences will be held on November 15th, 2025.', 'date': '2025-11-01'},
    {'id': 2, 'title': 'Sports Day', 'content': 'Annual sports day will be celebrated on December 5th, 2025.', 'date': '2025-11-15'},
    {'id': 3, 'title': 'Exam Schedule', 'content': 'Mid-term examinations will begin from November 20th, 2025.', 'date': '2025-11-10'}
]

# Semester Results Data (auto-generated per student)
def compute_grade(total_score):
    if total_score >= 75:
        return 'A'
    if total_score >= 65:
        return 'B'
    if total_score >= 55:
        return 'C'
    if total_score >= 45:
        return 'D'
    if total_score >= 40:
        return 'E'
    return 'F'

def find_teacher_name_for_subject(subject_name):
    for t in teachers:
        if t['subject'] == subject_name:
            return t['name']
    return 'Teacher TBD'

semester_results = {}
current_semester = 'First Term 2025'

for student in students:
    student_courses_results = []
    for subject_name in student['courses']:
        # Midterm out of 40, Exam out of 60
        midterm_score = random.randint(18, 40)
        exam_score = random.randint(35, 60)
        total_score = midterm_score + exam_score
        student_courses_results.append({
            'name': subject_name,
            'teacher': find_teacher_name_for_subject(subject_name),
            'midterm': midterm_score,
            'exam': exam_score,
            'total': total_score,
            'grade': compute_grade(total_score)
        })

    semester_results[student['id']] = {
        'semester': current_semester,
        'courses': student_courses_results
    }

def get_user_by_username(username):
    """Find user by username in students or teachers"""
    # Check students
    for student in students:
        if student['username'] == username:
            return {'type': 'student', 'user': student}
    
    # Check teachers
    for teacher in teachers:
        if teacher['username'] == username:
            return {'type': 'teacher', 'user': teacher}
    
    return None

def get_user_by_id(user_id, user_type):
    """Get user by ID and type"""
    if user_type == 'student':
        for student in students:
            if student['id'] == user_id:
                return student
    elif user_type == 'teacher':
        for teacher in teachers:
            if teacher['id'] == user_id:
                return teacher
    return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/portal')
def portal_home():
    if not session.get('logged_in'):
        flash('Please sign in to access the portal.', 'error')
        return redirect(url_for('signin'))
    return render_template('portal.html', announcements=announcements)

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/admissions')
def admissions_page():
    return render_template('admissions.html')

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        flash('Please log in to access your dashboard.', 'error')
        return redirect(url_for('signin'))
    
    user_type = session.get('user_type')
    
    if user_type == 'admin':
        return render_template('admin_dashboard.html', 
                             students=students, 
                             teachers=teachers, 
                             courses=courses, 
                             announcements=announcements)
    elif user_type == 'teacher':
        user_id = session.get('user_id')
        teacher = get_user_by_id(user_id, 'teacher')
        # Get courses taught by this teacher
        teacher_courses = [course for course in courses if course['teacher'] == teacher['name']]
        return render_template('teacher_dashboard.html', 
                             teacher=teacher, 
                             courses=teacher_courses, 
                             announcements=announcements)
    elif user_type == 'student':
        user_id = session.get('user_id')
        student = get_user_by_id(user_id, 'student')
        return render_template('student_home.html', 
                             student=student, 
                             announcements=announcements)
    else:
        flash('Invalid user type.', 'error')
        return redirect(url_for('home'))

@app.route('/results')
def results():
    if not session.get('logged_in'):
        flash('Please log in to view your results.', 'error')
        return redirect(url_for('signin'))
    
    user_type = session.get('user_type')
    user_id = session.get('user_id')
    
    if user_type == 'student':
        student = get_user_by_id(user_id, 'student')
        if student and user_id in semester_results:
            return render_template('student_results.html', 
                                 student=student, 
                                 results=semester_results[user_id])
        else:
            flash('Results not available.', 'error')
            return redirect(url_for('dashboard'))
    else:
        flash('This page is only available for students.', 'error')
        return redirect(url_for('dashboard'))

@app.route('/students')
def students_page():
    # Optional query params: q (name or username substring), grade
    query = request.args.get('q', '').strip().lower()
    grade = request.args.get('grade', '').strip().upper()

    filtered = students
    if query:
        filtered = [s for s in filtered if query in s['name'].lower() or query in s['username'].lower()]
    if grade and grade in classes:
        filtered = [s for s in filtered if s['grade'].upper() == grade]

    return render_template('students.html', students=filtered, q=query, grade=grade, classes=classes)

@app.route('/teachers')
def teachers_page():
    return render_template('teachers.html', teachers=teachers)

@app.route('/courses')
def courses_page():
    return render_template('courses.html', courses=courses)

@app.route('/announcements')
def announcements_page():
    return render_template('announcements.html', announcements=announcements)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check for admin login
        if username == 'admin' and password == 'password':
            session['logged_in'] = True
            session['username'] = username
            session['user_id'] = 0
            session['user_type'] = 'admin'
            session['user_name'] = 'Mr.OLANREWAJU BELLO'
            flash('Admin login successful!', 'success')
            return redirect(url_for('dashboard'))
        
        # Check for student or teacher login
        user_data = get_user_by_username(username)
        if user_data and user_data['user']['password'] == password:
            session['logged_in'] = True
            session['username'] = username
            session['user_id'] = user_data['user']['id']
            session['user_type'] = user_data['type']
            session['user_name'] = user_data['user']['name']
            flash(f'Welcome back, {user_data["user"]["name"]}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/student-home')
def student_home():
    if not session.get('logged_in') or session.get('user_type') != 'student':
        flash('Please log in as a student to access this page.', 'error')
        return redirect(url_for('signin'))
    
    user_id = session.get('user_id')
    student = get_user_by_id(user_id, 'student')
    if not student:
        flash('Student not found.', 'error')
        return redirect(url_for('home'))
    
    return render_template('student_home.html', student=student)

@app.route('/student-dashboard')
def student_dashboard():
    if not session.get('logged_in') or session.get('user_type') != 'student':
        flash('Please log in as a student to access this page.', 'error')
        return redirect(url_for('signin'))
    
    user_id = session.get('user_id')
    student = get_user_by_id(user_id, 'student')
    if not student:
        flash('Student not found.', 'error')
        return redirect(url_for('home'))
    
    return render_template('student_dashboard.html', 
                         student=student, 
                         announcements=announcements)

@app.route('/profile')
def profile():
    if not session.get('logged_in'):
        flash('Please log in to view your profile.', 'error')
        return redirect(url_for('login'))
    
    user_id = session.get('user_id')
    user_type = session.get('user_type')
    
    if user_type == 'admin':
        user_data = {'name': 'Mr.OLANREWAJU BELLO', 'type': 'admin'}
    else:
        user_data = get_user_by_id(user_id, user_type)
        if not user_data:
            flash('User not found.', 'error')
            return redirect(url_for('home'))
    
    return render_template('profile.html', user=user_data, user_type=user_type)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 