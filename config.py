import os
from dotenv import load_dotenv
load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))
from datetime import  timedelta

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY") #os.environ.get('SECRET_KEY') , os.environ.get('DATABASE_URI')
    JWT_SECRET_KEY= os.getenv("JWT_SECRET_KEY") #ref: https://stackoverflow.com/questions/46197050/flask-jwt-extend-validity-of-token-on-each-request
    JWT_ACCESS_TOKEN_EXPIRES= timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES= timedelta(days=30)
    JWT_TOKEN_LOCATION = ['headers','query_string']# 'cookies'
    QR_VERSION= os.getenv("QR_VERSION",3)
    BOX_SIZE = os.getenv("BOX_SIZE",8) 
    BORDER = os.getenv("BORDER",4)
    FILL_COLOR = os.getenv("FILL_COLOR","black")
    BACK_COLOR = os.getenv("BACK_COLOR","GreenYellow")