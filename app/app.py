from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    version = os.getenv("APP_VERSION", "dev")

    return {
        "application": "CloudOpsHub",
        "message": "CloudOpsHub is running!",
        "version": version,
        "environment": os.getenv("ENVIRONMENT", "local")
    }

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)