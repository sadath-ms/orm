
from . import create_app

apis_app = create_app()

if __name__ == '__main__':
    apis_app.run(debug=True)
