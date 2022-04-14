import os


if os.environ.get('GOOGLE_MAPS_KEY') is None:
    import API_Keys
    GOOGLE_MAPS_KEY = API_Keys.GOOGLE_MAPS_KEY

else:
    GOOGLE_MAPS_KEY = os.environ.get('GOOGLE_MAPS_KEY')


# database

basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get('FLASK_ENV') == 'development':
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
elif os.environ.get('FLASK_ENV') == 'production':
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    uri=os.environ.get('DATABASE_URL')
    if uri and uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    
    SQLALCHEMY_DATABASE_URI = uri