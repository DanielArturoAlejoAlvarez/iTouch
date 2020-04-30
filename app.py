from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database/task.db'
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(256))
    done = db.Column(db.Boolean)


@app.route('/')
def home():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


@app.route('/add-task', methods=['POST'])
def create():
    newTask = Task(content=request.form['content'], done=False)
    db.session.add(newTask)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/done/<id>')
def done(id):
    task = Task.query.filter_by(id=int(id)).first()
    task.done = not(task.done)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<id>')
def delete(id):
    task = Task.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('home'))




if __name__ == '__main__':
    app.run(debug=True)