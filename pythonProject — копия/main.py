from flask import Flask
from data import db_session
import sqlalchemy
import datetime
from sqlalchemy import orm
from data.User import User
from data.Jobs import Jobs


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/blogs.db")


def main():
    db_sess = db_session.create_session()
    user = Jobs()
    user.team_leader = 1
    user.job = 'deployment of residential modules 1 and 2'
    user.work_size = 15
    user.collaborators = '2, 3'
    user.is_finished = False
    db_sess.add(user)
    db_sess.commit()
    app.run()


if __name__ == '__main__':
    main()
