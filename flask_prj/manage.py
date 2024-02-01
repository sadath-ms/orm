# manage.py

from flask_migrate import Migrate
from apis_app import create_app, db

apis_app = create_app()
migrate = Migrate(apis_app, db)

if __name__ == '__main__':
    apis_app.run()
