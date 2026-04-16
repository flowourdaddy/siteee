from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "You have been fucked by Flowo & OPSanGZ (Thanks for IP):)"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)