# '''Here module description'''


# class QueryFactory:
#     '''Query factory'''
#     def movie_by_title(self, title: str) -> str:
#         '''Return query for filter movie by title'''
#         return f"""
#         SELECT title, country, release_year, listed_in, description
#           FROM netflix
#         WHERE title like '%{title}%'
#         """

#     def movie_by_year(self, year_from: int, year_to: int) -> str:
#         '''Return query for filter movie by year'''
#         return f"""
#         SELECT title, release_year
#           FROM netflix
#         WHERE release_year BETWEEN {year_from} AND {year_to}
#         LIMIT 100
#         """

#     def movie_by_rating(self, rating: tuple[str]) -> str:
#         '''Return query for filter movie by rating'''
#         proccessed_rating = list(map(lambda x: f"'{x}'", rating))
#         return f"""
#         SELECT title, rating, description
#           FROM netflix
#          WHERE rating IN ({",".join(proccessed_rating)})
#          ORDER BY date_added desc
#         """

#     def movie_by_genre(self, genre: str) -> str:
#         '''Return query for filter movie by genre'''
#         return f"""
#         SELECT title, description
#           FROM netflix
#          WHERE listed_in LIKE '%{genre}%'
#          ORDER BY date_added desc
#         """

#     def cast_more_then_two(self, first_actor: str, second_actor: str) -> str:
#         '''Query for filter movies with actors who plays together more then 2 films'''

#         return f'''
#             SELECT title, netflix.cast, description, count(*) as cast_count
#             FROM netflix
#             WHERE "cast" LIKE '%{first_actor}%' AND "cast" LIKE '%{second_actor}%'
#             GROUP BY "cast"
#             HAVING cast_count > 2
#         '''

#     def movie_by_title_year_genre(self, movie_type: str, release_year: int, genre: str) -> str:
#         '''Filter movie by year, type, genre'''
#         return f'''
#             SELECT title, description
#             FROM netflix
#             WHERE UPPER(type) = '{movie_type.upper()}' AND release_year = {release_year} AND UPPER(listed_in) LIKE '%{genre.upper()}%'
#             ORDER BY release_year DESC
#         '''
