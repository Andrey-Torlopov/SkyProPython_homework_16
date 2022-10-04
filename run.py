from flask import Flask, jsonify
from flask import render_template
import prettytable
from flask_sqlalchemy import SQLAlchemy
from app.dao import database
from app.api.views import api_blueprint

from app.dao.app_dao import AppDAO


app = Flask(__name__)
app.register_blueprint(api_blueprint)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found_404(error: Exception) -> str:
    '''Catch 404 error'''
    print(error)
    return render_template("404.html")


@app.errorhandler(500)
def not_found_500(error: Exception) -> str:
    '''Catch 500 error'''
    print(error)
    return render_template("500.html")


def debug_method():
    session = database.db.session()
    cursor = session.execute(f"SELECT * from {database.User.__tablename__}").cursor
    mytable = prettytable.from_db_cursor(cursor)
    mytable.max_width = 30
    print(mytable)
    cursor = session.execute(f"SELECT * from {database.Order.__tablename__}").cursor
    mytable = prettytable.from_db_cursor(cursor)
    mytable.max_width = 30
    print(mytable)
    cursor = session.execute(f"SELECT * from {database.Offer.__tablename__}").cursor
    mytable = prettytable.from_db_cursor(cursor)
    mytable.max_width = 30
    print(mytable)
    # a = session.query(database.User).all()
    # print("*"*50)
    # print(len(a))


appDAO = AppDAO()


if __name__ == '__main__':
    app.run(debug=True)
    database.setup_database()

    # a = appDAO.get_all_users()
    # dict_ary =
    # print(dict_ary)

    # data = jsonify(a)

    # debug_method()
