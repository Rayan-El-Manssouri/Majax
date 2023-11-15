# Import libry config
import configparser
import json
import logging

# Import Function
from Color.Bcolor import bcolors
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_session import Session
from werkzeug.security import  check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

# Utils
from Utils.HashMdp import HashMdp

# Disable logs
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Retrieving the config.ini file
config = configparser.ConfigParser()
config.read('./config.ini')

# Init app Flask
app = Flask(__name__)

# Default settings
configurations = {
    'SECRET_KEY': config['init']['SECRET_KEY'],
    'JWT_SECRET_KEY': config['init']['JWT_SECRET_KEY'],
    'SESSION_COOKIE_SAMESITE': config['init']['SESSION_COOKIE_SAMESITE'],
    'SESSION_TYPE': config['init']['SESSION_TYPE'],
    'SESSION_SECRET_KEY': config['init']['SESSION_SECRET_KEY']
}

app.config.update(configurations)

Session(app)
CORS(app)
JWTManager(app)

list_user_active = []

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if data and 'pseudo' in data and 'password' and 'email':
        file_path = './Majax/Database/Users.json'
        try:
            with open(file_path, "r") as existing_file:
                existing_data = json.load(existing_file)
        except FileNotFoundError:
            existing_data = []

        for user in existing_data:
            if user.get("email") == data['email']:
                print(user.get("email"))
                return jsonify({"error": "This e-mail is already in use"}), 400
    
        # Ajouter le nouveau contenu
        new_content = {
            "Pseudo": data['pseudo'],
            "Password_Hash": HashMdp.hash_mdp(data['password']),
            "email": data['email']
        }

        existing_data.append(new_content)
        # Écrire le contenu mis à jour dans le fichier
        with open(file_path, "w") as jsonFile:
            json.dump(existing_data, jsonFile, indent=4)
            return jsonify({"sucess": "Successful registration"}), 200
    else :
        return jsonify({"error": "Lack of arguments"}), 200

@app.route('/login', methods=['POST'])
def login():
    info = request.get_json()

    if 'email' not in info or 'password' not in info:
        return jsonify({"error": "Les champs 'email' et 'password' sont obligatoires"}), 400

    email = info['email']
    password = info['password']

    with open('./Majax/Database/Users.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

        for user in data:
            if user['email'] == email:
                if (check_password_hash(user['Password_Hash'], password) == True):
                    # Vérifier si l'email existe déjà dans la liste active
                    for active_user in list_user_active:
                        if active_user['email'] == email:
                            return jsonify({"error": "Utilisateur déjà connecté"}), 200

                    access_token = create_access_token(identity=email)
                    user_info = {
                        "email": email,
                        "password": password,
                        "pseudo": user['Pseudo'],
                        "jwt": access_token
                    }
                    list_user_active.append(user_info)
                    # Mettez à jour votre fichier JSON ou la base de données ici
                    return jsonify({"sucess": "Utilisateur connecté.", "access_token": access_token, "email": email, "Pseudo": user['Pseudo']}), 200

                return jsonify({"error": "Mot de passe incorrect"}), 401

        return jsonify({"error": "Email inconnu"}), 404
    
@app.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    info = request.get_json()
    email = info['email']

    # Recherche de l'utilisateur dans la liste
    user_to_remove = None
    for user in list_user_active:
        if user['email'] == email:
            user_to_remove = user
            break

    # Suppression de l'utilisateur s'il est trouvé
    if user_to_remove:
        list_user_active.remove(user_to_remove)
        return jsonify({'message': 'Utilisateur déconnecté avec succès'})
    else:
        return jsonify({'message': 'Utilisateur non trouvé'})

@app.route('/Fetch_Pseudo', methods=['POST'])
@jwt_required()
def Fetch_Pseudo():
    info = request.get_json()
    email = info['user_email']
    with open('./Majax/Database/Users.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for user in data:
            if (user['email'] == email):
                return jsonify({"pseudo": user['Pseudo']}), 200
            else :
                continue
        return jsonify({"message":"aucun compte trouvé"}), 400

@app.route('/CheckLogin', methods=['POST'])
@jwt_required()
def CheckLogin():
    info = request.get_json()
    email = info['email']
    for users in list_user_active:
        if users['email'] == email:
            return True, 200
    return False, 200
    
if __name__ == "__main__":
    print(f"{bcolors.OK}Welcome to server Majax from ", config['init']['NAME_SERVER'], f"and run in the port : ", config['init']['PORT'], f"{bcolors.RESET}")
    print("---------------------------------------------------")
    app.run('localhost', config['init']['PORT'])