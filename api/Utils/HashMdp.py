from werkzeug.security import generate_password_hash

class HashMdp:
    def hash_mdp(
        password: str
    ):
        """
        Generates a password hasher
        """
        return generate_password_hash(password)