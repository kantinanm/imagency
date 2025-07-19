from flask import Flask,current_app, jsonify
from flask_cors import CORS
from extensions import jwt
from config import Config


from routes import public,private,auth  # Import your routes here
#import routes.public




def create_app():
    app = Flask(__name__, template_folder='templates')
    #CORS(app)  # Enable CORS for all routes

    CORS(app,supports_credentials=True)
    app.config.from_object(Config)
    jwt.init_app(app)

    app.register_blueprint(public.bp) #group route mapping 
    app.register_blueprint(auth.bp, url_prefix='/auth') #group route mapping 
    app.register_blueprint(private.bp, url_prefix='/api/v1') #group route mapping

    
    # load user
    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_headers, jwt_data):
        identity = jwt_data["sub"]
        print(f"identity is {identity}")
        return identity


    # jwt error handlers
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_data):
        return jsonify({"message": "Token has expired", "error": "token_expired","status":False}), 401
        # return jsonify({
        #             "status": 401,
        #             "sub_status": 42,
        #             "msg": "The token has expired, please log in again."
        #         }), 401
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed", "error": "invalid_token","status":False}
            ),
            401,
        )
    
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        current_app.logger.error(f"missing_token_callback {str(error)}")
        return (
            jsonify(
                {
                    "message": "Request doesnt contain valid token",
                    "error": "authorization_header",
                    "debug":str(error),
                    "status":False
                }
            ),
            401,
        )
    
    return app