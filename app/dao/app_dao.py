from app.dao import database
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import relationship
# from sqlalchemy import or_, desc, func

class AppDAO:

    def get_all_users(self):
        with database.db.session() as session:
            data = session.query(database.User).all()
            result = list(map(lambda x: x.to_dict(), data))
            return result

        return {}
