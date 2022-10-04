import logging

from flask import Blueprint, jsonify
from app.dao.app_dao import AppDAO


api_blueprint = Blueprint('api_blueprint', __name__)
app_dao = AppDAO()


@api_blueprint.route('/', methods=['GET'])
def api_root() -> str:
    '''Root method of api'''
    return "All works well. You can send your requests..."


@api_blueprint.route("/users", methods=['GET'])
def all_users():
    logging.info('Запрос: /users')
    data = app_dao.get_all_users()
    print(data)
    # print(len(data))
    # return jsonify(data)
    return data


@api_blueprint.route("/users/<int:id>", methods=['GET'])
def user_by_id(id: int):
    logging.info(f'Запрос: /users/{id}')
    data = {
            "id": 1,
                    "first_name": "Hudson",
                    "last_name": "Pauloh",
                    "age": 31,
                    "email": "elliot16@mymail.com",
                    "role": "customer",
                    "phone": "6197021684"
                }
    return jsonify(data)



@api_blueprint.route("/orders", methods=['GET'])
def all_orders():
    logging.info('Запрос: /orders')
    data = [
            {
                "id": 0,
                "name": "Встретить тетю на вокзале",
                "description": "Встретить тетю на вокзале с табличкой. Отвезти ее в магазин, помочь погрузить покупки. Привезти тетю домой, занести покупки и чемодан в квартиру",
                "start_date": "02/08/2013",
                "end_date": "03/28/2057",
                "address": "4759 William Haven Apt. 194\nWest Corey, TX 43780",
                "price": 5512,
                "customer_id": 3,
                "executor_id": 6
            },
            {
                "id": 1,
                "name": "Позвать в гости девушку",
                "description": "Позвать в гости девушку и шикануть перед ней — заказать коробку конфет с доставкой на дом",
                "start_date": "01/24/2016",
                "end_date": "03/10/2076",
                "address": "9387 Grimes Green Apt. 801\nPagetown, NM 44165",
                "price": 2800,
                "customer_id": 18,
                "executor_id": 25
            },
            {
                "id": 2,
                "name": "Требуется уборка квартиры. Площадь",
                "description": "Требуется уборка квартиры. Площадь 85 м²: спальня, детская, гостиная, кухня. Санузел раздельный. Фотографии прикладываю.",
                "start_date": "04/19/2008",
                "end_date": "05/23/2099",
                "address": "93328 Davis Island\nRodriguezside, VT 16860",
                "price": 2320,
                "customer_id": 16,
                "executor_id": 19
            }
    ]

    return jsonify(data)



@api_blueprint.route("/orders/<int:id>", methods=['GET'])
def order_by_id(id: int):
    logging.info(f'Запрос: /orders/{id}')
    data = {
        "id": 1,
        "name": "Позвать в гости девушку",
        "description": "Позвать в гости девушку и шикануть перед ней — заказать коробку конфет с доставкой на дом",
        "start_date": "01/24/2016",
        "end_date": "03/10/2076",
        "address": "9387 Grimes Green Apt. 801\nPagetown, NM 44165",
        "price": 2800,
        "customer_id": 18,
        "executor_id": 25
    }
    return jsonify(data)



@api_blueprint.route("/offers", methods=['GET'])
def all_offers():
    logging.info('Запрос: /offers')
    data = [
            {
                "id": 0,
                "order_id": 36,
                "executor_id": 10
            },
            {
                "id": 1,
                "order_id": 35,
                "executor_id": 4
            },
            {
                "id": 2,
                "order_id": 35,
                "executor_id": 21
            },
            {
                "id": 3,
                "order_id": 47,
                "executor_id": 28
            },
            {
                "id": 4,
                "order_id": 18,
                "executor_id": 25
            }
    ]

    return jsonify(data)



@api_blueprint.route("/offers/<int:id>", methods=['GET'])
def offer_by_id(id: int):
    logging.info(f'Запрос: /orders/{id}')
    data = {
        "id": 1,
        "order_id": 35,
        "executor_id": 4
    }
    return jsonify(data)

# @api_blueprint.route("/api/movie/<title>", methods=['GET'])
# def movie_title(title: str):
#     '''Return json. Filter movie by title'''
#     logging.info('Запрос: /api/movie/%s', title)
#     data = app_dao.search_movie_by_title(title)
#     return jsonify(data)


# @api_blueprint.route("/api/movie/<int:year_from>/to/<int:year_to>", methods=['GET'])
# def movie_year_to_year(year_from: int, year_to: int):
#     '''Return json. Filter movie year to year'''
#     logging.info('Запрос: /api/movie/year/%s/to/%s', year_from, year_to)
#     data = app_dao.search_movies_by_release_year(year_from, year_to)
#     return jsonify(data)


# @api_blueprint.route("/api/rating/children", methods=['GET'])
# def movie_for_children():
#     '''Return json. Filter movie by rating'''
#     logging.info('Запрос: /api/rating/children')
#     data = app_dao.search_movies_by_rating(tuple(["G"]))
#     return jsonify(data)


# @api_blueprint.route("/api/rating/family", methods=['GET'])
# def movie_for_family():
#     '''Return json. Filter movie by rating'''
#     logging.info('Запрос: /api/rating/children')
#     data = app_dao.search_movies_by_rating(tuple(['G', 'PG', 'PG-13']))
#     return jsonify(data)


# @api_blueprint.route("/api/rating/adult", methods=['GET'])
# def movie_for_adult():
#     '''Return json. Filter movie by rating'''
#     logging.info('Запрос: /api/rating/children')
#     data = app_dao.search_movies_by_rating(tuple(['R', 'NC-17']))
#     return jsonify(data)


# @api_blueprint.route("/api/genre/<str:genre>", methods=['GET'])
# def movie_by_genre(genre: str):
#     '''Return json. Filter movie bt genre'''
#     logging.info('Запрос: /api/genre/%s', genre)
#     data = app_dao.search_movies_by_genre(genre)
#     return jsonify(data)

