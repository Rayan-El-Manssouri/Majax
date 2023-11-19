from sanic import Sanic
from sanic.response import json

app = Sanic()

@app.route('/')
@app.route('/<path:path>')
async def index(request, path=""):
    ip_address = request.ip
    return json({'hello': path, 'ip_address': ip_address})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)