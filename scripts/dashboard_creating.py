from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello, Flask!")

if __name__ == '__main__':
    # Explicitly set debug here
    app.run(host="0.0.0.0", port=5000, debug=True)
