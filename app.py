from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)

    if ip:
        ip = ip.split(",")[0].strip()

    print(f"REAL IP: {ip}")#render

    return f"Thanks | IP: {ip}"
    return("You have been fucked by OPSanGZ & FlowO")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
