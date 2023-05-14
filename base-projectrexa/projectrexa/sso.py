from flask import redirect, request, jsonify
from cryptography.fernet import Fernet
import base64
import json
import requests

def initiate_sso(callback_url:str, service:str,key_filename:str):
    json_data = {
        "callback_url": callback_url,
    }

    with open(f'{key_filename}.key', 'rb') as key_file:
        key = key_file.read()

    fernet_key = Fernet(key)

    encrypted_data = fernet_key.encrypt(json.dumps(json_data).encode())

    return redirect(
        f"https://sso.projectrexa.ml/sso/initialize?callback_token={base64.urlsafe_b64encode(encrypted_data).decode()}&service={service}"
    ), 200

def verify_callback(oauth_response:str,key_filename:str,request_time:int = 5):
    try:

        with open(f'{key_filename}.key', 'rb') as key_file:
            key = key_file.read()

        fernet_key = Fernet(key)

        decrypted_data = fernet_key.decrypt(
            base64.urlsafe_b64decode(oauth_response)).decode()
        json_data = json.loads(decrypted_data)

        response = requests.get(
                f"https://sso.projectrexa.ml/sso_token/verify?sso_token={json_data['sso_token']}",
                timeout=request_time).json()

        if  response["authenticated"] == "True":
            
            return_json =  {
                "authenticated": True,
                "user_info": json_data['user_info'],
                "message": response["message"]
            }
            return (return_json)
        
        return_json = {
            "authenticated": False,
            "user_info": None,
            "message": response["message"]
        }
        return (return_json)


    except Exception as e:
        raise Exception("Error in verifying callback | Error :",e)