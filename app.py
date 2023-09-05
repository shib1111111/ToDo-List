from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for, jsonify,flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os

db = SQLAlchemy()

def create_database():
    if not os.path.exists("instance/todos.db"):
        db.create_all()
        print("Created database!")
        
app = Flask(__name__)
app.config['SECRET_KEY'] = 'cf559170bf7a85a6f3f7e4dcfdb5bc11'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'

db.init_app(app)
# Push the app context
app.app_context().push()
create_database()
login_manager = LoginManager(app)


# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=False)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('tasks', lazy=True))

# Login Manager Configuration
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Routes
@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/signup.html', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        user = User.query.filter_by(username=username).first()
        if user and user.email == email and user.password == password :
            flash("Please Login , You already have account!!!",'success')
            return redirect(url_for('login'))
        
        elif user and user.email == email and user.password != password :
            flash("Please use other email and Username",'error')
            return redirect(url_for('register'))
        else:
            user = User(username=username,email = email, password=password)
            db.session.add(user)
            db.session.commit()
            flash("You are successfully signed up , now login ...",'success')
            return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            flash("You are successfully logged in...",'success')
            return redirect(url_for('tasks'))
        else:
            flash("Invalid Username or Password",'error')
    return render_template('signin.html')


@app.route('/tasks.html', methods=['GET', 'POST'])
@login_required
def tasks():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        task = Task(title = title, description=description, user=current_user)
        db.session.add(task)
        db.session.commit()
        flash("You are successfully added a new task...",'success')
        return redirect(url_for('tasks'))
    tasks = Task.query.filter_by(user=current_user).all()
    return render_template('tasks.html', tasks=tasks)



@app.route('/tasks/delete/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        if task.user == current_user:
            db.session.delete(task)
            db.session.commit()
            return jsonify({'success': True})
    return jsonify({'success': False})



@app.route('/tasks/update/<int:task_id>', methods=['POST'])
@login_required
def update_task(task_id):
    task = Task.query.get(task_id)
    if task:
        if task.user == current_user:
            new_title = request.json['title']
            new_description = request.json['description']
            task.title = new_title
            task.description = new_description
            db.session.commit()
            return jsonify({'success': True})
    return jsonify({'success': False})



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))



if __name__=="__main__":
    app.run(debug=False,host = '0.0.0.0')
