# '''Here module description'''
# import sqlite3

# from app.dao.query_factory import QueryFactory
# from app.models.movie import Movie


# class AppDAO:
#     '''Data provider class'''

#     _databse_name: str = './static/netflix.db'

#     def search_movie_by_title(self, title: str) -> list[Movie]:
#         '''Search moviews by name'''
#         sql_query = QueryFactory().movie_by_title(title=title)

#         with sqlite3.connect(self._databse_name) as con:
#             cur = con.cursor()
#             ex_cur = cur.execute(sql_query)
#             result: list[Movie] = []

#             for row in ex_cur.fetchall():
#                 print(row)
#                 movie = Movie(*row)
#                 result.append(movie)
#         return result

#     def search_movies_by_release_year(self, year_from: int, year_to: int) -> list[dict[str, int]]:
#         """
#         Search movies bt release year.
#         Return array of dictionary:
#         [
#             {"title":"title",
#             "release_year": 2021},
#             {"title":"title",
#             "release_year": 2020}
#         ]
#         """
#         sql_query = QueryFactory().movie_by_year(year_from, year_to)

#         with sqlite3.connect(self._databse_name) as con:
#             cur = con.cursor()
#             ex_cur = cur.execute(sql_query)
#             result: list[dict[str, int]] = []

#             for row in ex_cur.fetchall():
#                 result.append({"title": row[0], "release_year": row[1]})
#         return result

#     def search_movies_by_rating(self, rating: tuple[str]) -> list[dict[str, str]]:
#         """
#         Search movies woith rating
#         Return array of dictionary:
#         [
#             {
#                 "title":"title",
#                 "rating": "rating",
#                 "description":"description"
#                 }
#          ]
#         """
#         sql_query = QueryFactory().movie_by_rating(rating)
#         with sqlite3.connect(self._databse_name) as con:
#             cur = con.cursor()
#             result: list[dict[str, str]] = []
#             ex_cur = cur.execute(sql_query)

#             for row in ex_cur.fetchall():
#                 print(row)
#                 result.append(
#                     {
#                         "title": row[0],
#                         "rating": row[1],
#                         "description": row[2]
#                     })

#         return result

#     def search_movies_by_genre(self, genre: str) -> list[dict[str, str]]:
#         """
#         Search movies by genre
#         Return array of dictionary:
#         [
#             {
#                 "title":"title",
#                 "description":"description"
#             }
#          ]
#         """
#         sql_query = QueryFactory().movie_by_genre(genre)

#         with sqlite3.connect(self._databse_name) as con:
#             cur = con.cursor()
#             result: list[dict[str, str]] = []
#             ex_cur = cur.execute(sql_query)

#             for row in ex_cur.fetchall():
#                 print(row)
#                 result.append(
#                     {
#                         "title": row[0],
#                         "description": row[1]
#                     }
#                 )

#         return result

# def search_movies_by_type_year_genre(self, movie_type: str, release_year: int, genre: str) -> list[dict[str, str]]:
#         """
#         Return array of dictionary:
#         [
#             {
#                 "title":"title",
#                 "description":"description"
#             }
#          ]
#         """

#         sql_query = QueryFactory().movie_by_title_year_genre(movie_type, release_year, genre)

#         with sqlite3.connect(self._databse_name) as con:
#             cur = con.cursor()
#             result: list[dict[str, str]] = []
#             ex_cur = cur.execute(sql_query)

#             for row in ex_cur.fetchall():
#                 print(row)
#                 result.append(
#                     {
#                         "title": row[0],
#                         "description": row[1]
#                     }
#                 )

#         return result

#     def search_movies_by_actors(self, actors: list[str]) -> list[dict[str, str]]:
#         """
#         Search movies by actors who plays more then 2 movies
#         Return array of dictionary:
#         [
#             {
#                 "title":"title",
#                 "description":"description"
#             }
#          ]
#         """
#         assert len(actors) == 2, "Should be 2 actors in list"

#         sql_query = QueryFactory().cast_more_then_two(actors[0], actors[-1])
#         print(sql_query)
#         return []

#         # with sqlite3.connect(self._databse_name) as con:
#         #     cur = con.cursor()
#         #     result: list[dict[str, str]] = []
#         #     ex_cur = cur.execute(sql_query)

#         #     for row in ex_cur.fetchall():
#         #         print(row)
#         #         result.append(
#         #             {
#         #                 "title": row[0],
#         #                 "description": row[1]
#         #             }
#         #         )

#         # return result