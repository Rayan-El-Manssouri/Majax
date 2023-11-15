import configparser
from Crypto.PublicKey import RSA
import jwt
import base64

config = configparser.ConfigParser()
config.read('./config.ini')

class JwtManagerNew():
    @staticmethod
    def generate_new_jwt_key():
        print("Création de la clé RSA ....")
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()

        # Créer un JWT avec RS256
        token_payload = {
            "admin": True,
            "Users": "mercure-app.com"
        }

        token = jwt.encode(token_payload, private_key, algorithm='RS256')
        print("Clé RSA complétée !")
        return token, public_key

    @staticmethod
    def update_jwt_key():
        # Générer une nouvelle clé JWT (remplacez cela par votre logique de génération)
        new_jwt_token, public_key = JwtManagerNew.generate_new_jwt_key()
        
        # Convertir la clé publique en une chaîne d'octets (bytes)
        public_key_bytes = base64.b64encode(public_key).decode()

        # Mettre à jour la clé JWT dans le fichier de configuration
        config.set('identity', 'JWT_KEY', new_jwt_token)
        config.set('identity', 'public_key', public_key_bytes)

        # Écrire les modifications dans le fichier
        with open('./config.ini', 'w') as config_file:
            config.write(config_file)


    @staticmethod
    def decode_token(token):
        token = config['identity']['JWT_KEY']
        public_key_bytes = config['identity']['public_key']
        
        # Convertir la clé publique en une chaîne d'octets (bytes)
        public_key = base64.b64decode(public_key_bytes)
        
        decoded_token = jwt.decode(token, public_key, algorithms=['RS256'])
        print("Token décodé :", decoded_token)

    def verify_token(headers: str, data):
        """
        Function to retrieve headers and Authorization key to verify RSA key authenticity
        """
        body = str(data)
        print(body)
        token = headers.get('Authorization')
        if token != config['identity']['public_key']:
            return False
        if token is None:
            return False
        try:
            JwtManagerNew.decode_token(token)
            return True
        except jwt.ExpiredSignatureError:
            return False
        except jwt.InvalidTokenError:
            return False