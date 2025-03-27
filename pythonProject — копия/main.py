from flask import Flask
from data import db_session
import sqlalchemy
import datetime
from sqlalchemy import orm
from data.User import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/blogs.db")


def main():
    db_sess = db_session.create_session()
    k = '_'
    for i in range(3):
        user = User()
        user.surname = f"Scott{k * i}"
        user.name = f"Ridley{k * i}"
        user.age = 21
        user.position = f"captain{k * i}"
        user.speciality = f"research engineer{k * i}"
        user.address = f"module_1{k * i}"
        user.email = f"scott_chief{k * i}@mars.org"
        db_sess.add(user)
    db_sess.commit()
    app.run()


if __name__ == '__main__':
    main()
