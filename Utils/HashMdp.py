from werkzeug.security import generate_password_hash

class HashMdp:
    def hash_mdp(password):
     return generate_password_hash(password)