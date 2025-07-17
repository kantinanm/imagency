from flask import Blueprint, request ,jsonify, redirect, render_template, abort
from dotenv import load_dotenv
load_dotenv()
import os
from service import utility


APP_NAME = os.getenv("MY_APP")

bp = Blueprint("public", __name__) 

@bp.route('/')
def index():
    return jsonify({"message": "Welcome  sir Demo?", "Server": "is_runing"}), 200

@bp.route("/home",methods=['GET'])
def home():
    return "Hello,"+APP_NAME+" World!"

@bp.route("/about",methods=['GET'])
def about():
    return "Hello, About!"

@bp.route("/tab", methods=['GET'])
def tab():
    return render_template("pages/tab.html")

@bp.route('/generate', methods=['GET'])
def generate():
    raw_data = utility.generate_qr()
    return jsonify({'ok':'true',"message": "QR Code generated successfully", "raw_data": raw_data}), 200

@bp.route("/qr", methods=['GET'])
def qr_interface():
    raw_data = utility.generate_qr()
    result={"message": "QR Code generated successfully", "raw_data": raw_data}
    return render_template("pages/qr_ui.html",data=result)