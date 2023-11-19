from http.server import BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Récupère l'adresse IP du client à partir de l'en-tête X-Forwarded-For
        client_ip = self.headers.get('X-Forwarded-For') or self.client_address[0]

        # Envoie une réponse HTTP 200 OK avec l'adresse IP du client
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response_content = f"Votre adresse IP est : {client_ip}"
        self.wfile.write(response_content.encode())

if __name__ == '__main__':
    from http.server import HTTPServer

    # Spécifie le port sur lequel le serveur écoutera
    port = 8000

    # Crée une instance du serveur en utilisant MyHandler comme gestionnaire
    server = HTTPServer(('localhost', port), MyHandler)

    # Affiche un message pour indiquer que le serveur est en cours d'exécution
    print(f"Serveur en cours d'exécution sur le port {port}")

    # Laisse le serveur tourner en continu
    server.serve_forever()