import re

def est_email(val):
    pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
    return bool(pattern.match(val))

# Exemple d'utilisation
champ = input("Entrez une adresse e-mail : ")

if est_email(champ):
    print("C'est une adresse e-mail valide.")
else:
    print("Ce n'est pas une adresse e-mail valide.")