import os


if os.environ.get('GOOGLE_MAPS_KEY') is None:
    import API_Keys
    GOOGLE_MAPS_KEY = API_Keys.GOOGLE_MAPS_KEY

else:
    GOOGLE_MAPS_KEY = os.environ.get('GOOGLE_MAPS_KEY')