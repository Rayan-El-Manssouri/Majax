from Crypto.PublicKey import RSA
import jwt

# Générer une paire de clés RSA
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Créer un JWT avec RS256
token_payload = {
    "admin": True,
    "Users": "mercure-app.com"
}

token = jwt.encode(token_payload, private_key, algorithm='RS256')

# Correction : Utiliser la clé publique comme un objet, pas une chaîne
decoded_token = jwt.decode(token, public_key, algorithms=['RS256'])

print('JWT token:', token)
print("JWT Token decode :", decoded_token)