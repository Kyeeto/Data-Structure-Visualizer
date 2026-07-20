from flask import Flask
from flask_cors import CORS
from api.structureRoutes import structureAPI
from api.algorithmRoutes import algorithmAPI

app = Flask(__name__)
CORS(app)
app.register_blueprint(structureAPI, url_prefix = "/api/structures")
app.register_blueprint(algorithmAPI, url_prefix = "/api")

if __name__ == "__main__":
    app.run(debug=True)
