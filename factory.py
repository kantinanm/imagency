from flask import Flask, jsonify, render_template
from flask_cors import CORS



from routes import public,private  # Import your routes here
#import routes.public





def create_app():
    app = Flask(__name__, template_folder='templates')
    CORS(app)  # Enable CORS for all routes
    app.register_blueprint(public.bp) #group route mapping 
    app.register_blueprint(private.bp, url_prefix='/api/v1') #group route mapping
    return app