from flask import Flask
from flask import render_template

import prettytable
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy


from sqlalchemy.orm import relationship

from app.api.views import api_blueprint

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


# Database models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text(100))
    last_name = db.Column(db.Text(100))
    age = db.Column(db.Integer)
    email = db.Column(db.Text(50))
    role = db.Column(db.Text(50))
    phone = db.Column(db.Text(20))
    offers = relationship('Offer')
    # orders = relationship('Order', backref='customer', lazy=True)

class Offer(db.Model):
    __tablename__ = 'offers'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("users.id"))


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(100))
    description = db.Column(db.Text(200))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    address = db.Column(db.Text(200))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("users.id"))


def main():
    db.drop_all()
    db.create_all()
    session = db.session()


    user1 = User(
        first_name="First1",
        last_name="Last1",
        age=20,
        email="foo1@test.ru",
        role="C",
        phone="+7-111111111"
    )

    user2 = User(
        first_name="First2",
        last_name="Last2",
        age=30,
        email="foo2@test.ru",
        role="E",
        phone="+7-222222222"
    )

    order1 = Order(
        name="order #1",
        description="Todo",
        start_date=datetime.strptime('2022-10-01', '%Y-%m-%d'),
        end_date=datetime.strptime('2022-10-03', '%Y-%m-%d'),
        address="Address1",
        price=100,
        customer_id=1
        )

    offer1 = Offer(
        order_id=1,
        executor_id=2
    )

    users = (user1, user2)
    orders = (order1,)
    offers = (offer1,)
    with db.session.begin():
        db.session.add_all(users)
        db.session.add_all(orders)
        db.session.add_all(offers)

    print("")
    print("-"*30)
    off1 = Offer.query.get(1)
    print(off1)

    print("-"*30)
    print("")

    cursor = session.execute(f"SELECT * from {User.__tablename__}").cursor
    mytable = prettytable.from_db_cursor(cursor)
    mytable.max_width = 30
    print(mytable)
    cursor = session.execute(f"SELECT * from {Order.__tablename__}").cursor
    mytable = prettytable.from_db_cursor(cursor)
    mytable.max_width = 30
    print(mytable)
    cursor = session.execute(f"SELECT * from {Offer.__tablename__}").cursor
    mytable = prettytable.from_db_cursor(cursor)
    mytable.max_width = 30
    print(mytable)


if __name__ == '__main__':
    # app.run(debug=True)
    main()
