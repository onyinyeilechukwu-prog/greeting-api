from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! Welcome to the Greeting API."

@app.route("/health")
def health():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"status": "healthy", "checked_at": current_time}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
