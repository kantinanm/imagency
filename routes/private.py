from flask import Blueprint,current_app, request ,jsonify, redirect, render_template, abort
from dotenv import load_dotenv
load_dotenv()
import os
from service import utility

bp = Blueprint("private", __name__) 

@bp.route("/generate",methods=['POST'])

def generate_by_payload():#current_user
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

            if False is None:
                raise  Exception("User account don't match")

            smt_url=data['url']
            token=data['token']
            url=smt_url+"?token="+token

            back_color=data['back_color'] if 'back_color' in data else os.getenv("BACK_COLOR", "GreenYellow")

            #print(data)
            print("smt_url : "+smt_url)
            print("token : "+token)
            print("url : "+url)
            print("back_color : "+back_color)


            options = {
                'data': url,
                'version': os.getenv("VERSION", 3),
                'box_size': os.getenv("BOX_SIZE", 8),# current_app.config.get('BOX_SIZE', 8),
                'border': os.getenv("BORDER", 4),   
                'fill_color': os.getenv("FILL_COLOR", "black"), #current_app.config.get('FILL_COLOR', 'black'),
                'back_color':back_color
                #'back_color': os.getenv("BACK_COLOR", "GreenYellow")
            }

            try:
                raw_data = utility.generate_qr_v2(options)  
            except Exception as e:
                print("Error generating QR code: ", str(e))
                return jsonify({'ok':'false',"message": "Error generating QR code", "error": str(e)}), 500

            
            response = {'ok':'true', "raw_data": raw_data, "message": "QR Code generated successfully"}

            return jsonify(response)

        except Exception as e:
            print(str(e))
            response = {'ok':'false','error message':str(e)}
            return response
    else:
        response = {'ok':'false','message':'Content-Type not supported!'}
        return response