import datetime
from flask import Flask, url_for, request, render_template, redirect
from data import db_session
from data.job import Job

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def works_log():
    db_sess = db_session.create_session()
    works = db_sess.query(Job)
    return render_template("works_log.html", jobs=works)


def main(db_name):
    db_session.global_init(db_name)
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main('db/blogs.db')