from flask import Blueprint,current_app, request ,jsonify, redirect, render_template, abort
#from flask_jwt_extended import current_user,jwt_required
from dotenv import load_dotenv
load_dotenv()
import os
from service import utility

bp = Blueprint("private", __name__) 

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

@bp.route("/generate",methods=['POST'])
def generate_by_payload():#current_user
    current_app.logger.info("executed generate_by_payload")
    content_type = request.headers.get('Content-Type')

    """ Generate a QR code with the given options.
    Args:
        options (dict): A dictionary containing the options for the QR code.
            It should contain 'data', 'version', 'error_correction', 'box_size', and 'border'.
    Returns:
        str: The base64 encoded string of the generated QR code image.  
    """
    
    if (content_type == 'application/json'):

        try:
            data=request.get_json()
            print(data)

            if False :
                raise  Exception("User account don't match")
            
            if not data or "secret" not in data or "nunet" not in data or "url" not in data or "ref_id" not in data:
                return jsonify({"error":"Missing 'secret' or 'nunet' or 'url' or 'ref_id'"})
            elif data['secret'] != os.getenv("SECRET_KEY"):
                return jsonify({"error":"Invalid 'secret'"}), 401
    
            
            #create access token
            access_token = create_access_token(identity=data['nunet'])
            current_app.logger.info(f"Access Token: {access_token}")
            #create refresh token
            refresh_token = create_refresh_token(identity=data['nunet'])
            current_app.logger.info(f"Refresh Token: {refresh_token}")
            

            url=data['url']


            #print(data)

            print("url : "+url)
   


            options = {
                'data': url,
                'qr_version': data['qr_version'] if 'qr_version' in data else current_app.config.get('QR_VERSION', 3) ,
                'box_size': data['box_size'] if 'box_size' in data else current_app.config.get('BOX_SIZE', 8) ,# current_app.config.get('BOX_SIZE', 8), #BOX_SIZE
                'border': data['border'] if 'border' in data else current_app.config.get('BORDER', 4),  #BORDER ,os.getenv("BORDER", 4),  
                'fill_color': data['fill_color'] if 'fill_color' in data else current_app.config.get('FILL_COLOR', 'black'), #current_app.config.get('FILL_COLOR', 'black'),
                'back_color':data['back_color'] if 'back_color' in data else current_app.config.get('BACK_COLOR', 'GreenYellow')#os.getenv("BACK_COLOR", "GreenYellow")
            }

            try:
                raw_data = utility.generate_qr_v2(options)  
            except Exception as e:
                print("Error generating QR code: ", str(e))
                return jsonify({'ok':'false',"message": "Error generating QR code", "error": str(e)}), 500

            
            response = {'ok':'true',"access_token":access_token,"refresh_token":refresh_token, "raw_data": raw_data, "message": "QR Code generated successfully"}

            return jsonify(response)

        except Exception as e:
            print(str(e))
            response = {'ok':'false','error message':str(e)}
            return response
    else:
        response = {'ok':'false','message':'Content-Type not supported!'}
        return response
    
@bp.route("/info",methods=['GET'])
@jwt_required() #@token_required
def check():
    return "Hello, info!"