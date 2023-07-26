from decouple import config


class Config(object):
    APP_SECRET_KEY = config('APP_SECRET_KEY', default="APP_SECRET_KEY")

    DB_NAME = config('DB_NAME',default="app")
    DB_USERNAME = config('DB_USER', default="user")
    DB_HOST = config('DB_HOST', default="db")
    DB_PASSWORD = config('DB_PASSWORD', default="password")
    DB_URL = f"postgresql+psycopg2://{DB_HOST}/{DB_NAME}?user={DB_USERNAME}&password={DB_PASSWORD}"