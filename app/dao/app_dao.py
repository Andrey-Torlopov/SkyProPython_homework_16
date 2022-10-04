from app.dao import database
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import relationship
# from sqlalchemy import or_, desc, func

class AppDAO:

    def get_all_users(self):
        result = database.User.query.all()
        return result
