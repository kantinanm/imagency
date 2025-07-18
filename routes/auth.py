from flask import Blueprint, jsonify, request, make_response
from flask import current_app as my_app
import json
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt,
    current_user,
    #set_access_cookies,
    #unset_jwt_cookies,
    get_jwt_identity,
)

bp = Blueprint("auth", __name__) 

@bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh_access():
    #identity = get_jwt_identity()
    current_user = get_jwt_identity()

    new_access_token = create_access_token(identity=current_user)
    print(f"refresh token with user {current_user} ,token :{new_access_token}")

    return jsonify({"access_token": new_access_token,"current_user": current_user}), 200

@bp.route('/logout', methods=["GET"])
@jwt_required(verify_type=False) 
def logout_user():
    jwt = get_jwt()
    

    jti = jwt['jti']
    user = jwt['sub']
    
    token_type = jwt['type']
    print(f"uudi[jti] :{jti}")
    print(f"{user} logout :{jwt}")

    response={"message": f"{token_type} token revoked successfully"}

    #unset_jwt_cookies(response)

    return jsonify(response) , 200