# iTouch (Flask-SQLAlchemy)

## Description

This repository is a Software of Application with Python, Flask, SQLAlchemy (ORM) and SQLite.

## Installation

Using Flask Framework, SQLAlchemy, SQLite,etc preferably.

## DataBase

Using SQLite3 preferably.

## Apps

Using pipenv.

## Usage

```html
$ git clone https://github.com/DanielArturoAlejoAlvarez/iTouch.git
[NAME APP]
```

Follow the following steps and you're good to go! Important:

![alt text](https://user-images.githubusercontent.com/41679407/60867874-5ea4e080-a25e-11e9-9976-cc61cbd8712f.gif)

## Coding

### Config

```python
...
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
...
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/DanielArturoAlejoAlvarez/iTouch. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
````
