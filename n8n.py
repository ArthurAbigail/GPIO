from flask import Flask

app = Flask(__name__)
@app.route("/buzzer", methods=["GET"])
def buzzer_toggle():
    return "Hello"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)