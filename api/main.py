# # Import libry
# import configparser
# import json
# import logging
# import click

# # Import Function
# from Color.Bcolor import bcolors
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from flask_session import Session
# from werkzeug.security import  check_password_hash
# from flask_jwt_extended import JWTManager, create_access_token, jwt_required

# # # Utils
# # from Utils.HashMdp import HashMdp
# # from Utils.ValideEmail import est_email
# # from Utils.Jwt_keys.GenerateNewJwt import JwtManagerNew

# # Empty list creation for active
# list_user_active = []

# # Retrieving the config.ini file
# config = configparser.ConfigParser()
# config.read('./config.ini')

# # Init app Flask
# app = Flask(__name__)
# log = logging.getLogger('werkzeug')

# log.setLevel(logging.ERROR)

# def secho(text, file=None, nl=None, err=None, color=None, **styles):
#     pass

# def echo(text, file=None, nl=None, err=None, color=None, **styles):
#     pass

# click.echo = echo
# click.secho = secho

# # Default settings
# configurations = {
#     'SECRET_KEY': config['init']['SECRET_KEY'],
#     'JWT_SECRET_KEY': config['init']['JWT_SECRET_KEY'],
#     'SESSION_COOKIE_SAMESITE': config['init']['SESSION_COOKIE_SAMESITE'],
#     'SESSION_TYPE': config['init']['SESSION_TYPE'],
#     'SESSION_SECRET_KEY': config['init']['SESSION_SECRET_KEY']
# }

# app.config.update(configurations)

# PORT = config['init']['PORT']

# Session(app)
# CORS(app)
# JWTManager(app)

# JwtManagerNew.update_jwt_key()


# # Route Resgister PRIVATE
# @app.route('/register', methods=['POST'])
# def register():
#     """
#     This route needs the PUBLIC_KEY key in config.ini to work.
#     """
#     data = request.get_json()
#     email = data['email']
#     pseudo = data['pseudo']
#     password = data['password']
    
#     # Vérifier le token
#     if not JwtManagerNew.verify_token(request.headers, data):
#         print("Tentative d'acces ...")
#         return jsonify({"error": "Unauthorized"}), 401
    
#     if email is not None and password is not None and pseudo is not None :
#         if(est_email(email=email)):
#             file_path = './Database/Users.json'
#             try:
#                 with open(file_path, "r") as existing_file:
#                     existing_data = json.load(existing_file)
#             except FileNotFoundError:
#                 existing_data = []

#             for user in existing_data:
#                 if user.get("email") == data['email']:
#                     return jsonify({"error": "This e-mail is already in use"}), 400

#             # Ajouter le nouveau contenu
#             new_content = {
#                 "Pseudo": data['pseudo'],
#                 "Password_Hash": HashMdp.hash_mdp(data['password']),
#                 "email": data['email']
#             }
#             existing_data.append(new_content)
#             # Écrire le contenu mis à jour dans le fichier
#             with open(file_path, "w") as jsonFile:
#                 json.dump(existing_data, jsonFile, indent=4)
#                 return jsonify({"sucess": "Successful registration"}), 200
#         else :
#             return jsonify({"error": "Email incorrect ou mauvaise format"})
#     else:
#         return jsonify({"error": "Incorrect Arguments"})

# @app.route('/login', methods=['POST'])
# def login():
#     info = request.get_json()

#     if 'email' not in info or 'password' not in info:
#         return jsonify({"error": "Les champs 'email' et 'password' sont obligatoires"}), 400

#     email = info['email']
#     password = info['password']

#     with open('./Database/Users.json', 'r', encoding='utf-8') as f:
#         data = json.load(f)

#         for user in data:
#             if user['email'] == email:
#                 if (check_password_hash(user['Password_Hash'], password) == True):
#                     # Vérifier si l'email existe déjà dans la liste active
#                     for active_user in list_user_active:
#                         if active_user['email'] == email:
#                             return jsonify({"error": "Utilisateur déjà connecté"}), 200

#                     access_token = create_access_token(identity=email, expires_delta=False)
#                     user_info = {
#                         "email": email,
#                         "password": password,
#                         "pseudo": user['Pseudo'],
#                         "jwt": access_token
#                     }
#                     list_user_active.append(user_info)
#                     # Mettez à jour votre fichier JSON ou la base de données ici
#                     return jsonify({"sucess": "Utilisateur connecté.", "access_token": access_token, "email": email, "Pseudo": user['Pseudo']}), 200
#                 return jsonify({"error": "Mot de passe incorrect"}), 401
#         return jsonify({"error": "Email inconnu"}), 404
    
# @app.route('/logout', methods=['POST'])
# @jwt_required()
# def logout():
#     info = request.get_json()
#     email = info['email']

#     # Recherche de l'utilisateur dans la liste
#     user_to_remove = None
#     for user in list_user_active:
#         if user['email'] == email:
#             user_to_remove = user
#             break

#     # Suppression de l'utilisateur s'il est trouvé
#     if user_to_remove:
#         list_user_active.remove(user_to_remove)
#         return jsonify({'sucess': 'Utilisateur déconnecté avec succès'})
#     else:
#         return jsonify({'error': 'Utilisateur non trouvé'})

# @app.route('/Fetch_Pseudo', methods=['POST'])
# @jwt_required()
# def Fetch_Pseudo():
#     info = request.get_json()
#     email = info['user_email']
#     with open('./Majax/Database/Users.json', 'r', encoding='utf-8') as f:
#         data = json.load(f)
#         for user in data:
#             if (user['email'] == email):
#                 return jsonify({"pseudo": user['Pseudo']}), 200
#             else :
#                 continue
#         return jsonify({"error":"aucun compte trouvé"}), 400

# @app.route('/CheckLogin', methods=['POST'])
# @jwt_required()
# def CheckLogin():
#     info = request.get_json()
#     email = info['email']
#     for users in list_user_active:
#         if users['email'] == email:
#             return True, 200
#     return False, 200

# @app.route('/', methods=['GET'])
# def home():
#     return jsonify({"error": "Missing acces"})
    
# if __name__ == "__main__":
#     print(f"{bcolors.OKBLUE}Starting developement server", f"{bcolors.RESET}")
#     print(f"{bcolors.OK}Api run in the url : http://localhost:{PORT} {bcolors.RESET}")
#     app.run('localhost', config['init']['PORT'])


from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello word majax ! '