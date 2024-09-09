from app.main import app  # Importa tu aplicación FastAPI
import json

with open("./api-rtr/openapi.json", "w") as f:
    json.dump(app.openapi(), f)
