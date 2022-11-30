from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from app import db, app
from .models import Student, User
from .forms import StudentForm, UserForm


def students_list():
    students = Student.query.all()
    return render_template('students_list.html', students=students)

@login_required
def student_create():
    form = StudentForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            student = Student()
            form.populate_obj(student)
            db.session.add(student)
            db.session.commit()
            flash('Студент успешно сохранен', 'success')
            return redirect(url_for('students_list'))
    return render_template('student_form.html', form=form)


def student_detail(id):
    student = Student.query.get(id)
    return render_template('student_detail.html', student=student)

@login_required
def student_update(id):
    student = Student.query.get(id)
    form = StudentForm(request.form, obj=student)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(student)
            db.session.add(student)
            db.session.commit()
            return redirect(url_for('students_list'))
    return render_template('student_form.html', form=form)

@login_required
def student_delete(id):
    student = Student.query.get(id)
    if request.method == 'POST':
        db.session.delete(student)
        db.session.commit()
        return redirect(url_for('students_list'))
    return render_template('student_delete.html', student=student)


def register_view():
    form = UserForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User()
            form.populate_obj(user)
            db.session.add(user)
            db.session.commit()
            flash(f'Polzovatel {user.username} успешно сохранен', 'success')
            return redirect(url_for('login'))
    return render_template('user_form.html', form=form)

def login_view():
    logout_user()
    form = UserForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            # user = User()
            # form.populate_obj(user)
            user = User.query.filter_by(username=request.form.get('username')).first()
            if user and user.check_password(request.form.get('password')):
                login_user(user)
                flash('Uspeshno avtorizovan!', 'primary')
                return redirect(url_for('students_list'))
            else:
                flash('Ne pravilno vveden login ili parol', 'danger')
    return render_template('user_form.html', form=form)

def logout_view():
    logout_user()
    return redirect(url_for('login'))








