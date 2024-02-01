from apis_app import create_app, db


apis_app = create_app()



if __name__ == '__main__':
    apis_app.run(debug=True)