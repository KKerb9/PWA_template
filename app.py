from flask import Flask


print(f"Flask version: {version('flask')}")
app = Flask(__name__, template_folder="templates/", static_folder="static/")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)